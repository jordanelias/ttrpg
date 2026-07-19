# Internal-Polity Precedents (v1) — governance-modes · caste/franchise/conflict · heresy/suppression

## Status: research provenance (FILED) — 2026-07-13 · ED-IN-0051

Distilled from three web-/scholarship-grounded threads, **"without pattern matching"** — actionable
findings + REAL/SURFACE verdicts, feeding `precedent_fix_catalog_v1.md` (GAP-C2, GAP-F1..F5, GAP-G1/G2).
Full reports are the session's task transcripts. Each thread first checked the corpus to **extend, not
duplicate** the 2026-06-28 deliberation trilogy, the four-modes review, and the 07-08/07-09 dockets.

---

## A · Governance-mode taxonomy (→ GAP-C2, GAP-C1, GAP-C4)

**Core ruling:** `governance_mode` is a **FLAG** parallel to (not the same as) the built *manager-type*
enum. **Property-class, sortition, and acclamation are PARAMETERS, not modes** (roster-selection or
termination conditions usable *inside* a mode) — matching the four-modes review's own ruling. Each mode
names **which of Valoria's 4 contest-games** (Agôn WIRED / Negotiation STUB / Inquiry STUB / Consensus
STUB) resolves its business — and some modes correctly resolve to **no game at all** (fiat = a Directive
FLAG; the real contest is displaced to Standing/Ascendancy/Succession machinery — that is a *correct*
answer, not a missing build).

**Recommended enumerated `governance_mode` FLAG domain** (fills the empty palette in
`governance_type_registry §2`):

| value | resolves via | start-active vs latent | anchor |
|---|---|---|---|
| AUTOCRATIC_FIAT | none (Directive FLAG) | start-active (Crown default) | royal decree |
| ROYAL_COURT_APPOINTMENT | none (Directive per link; hostage-kin/Court-Attendance exist) | start-active | Philip II governors; Versailles |
| OLIGARCHIC_COUNCIL | Agôn on a narrow peer roster; supports an *elect-inward* sub-committee | start-active | Venice Senate/Ten; Spartan gerousia |
| LANDHOLDER_FRANCHISE | Agôn, weighted/blocs, **+ early-termination-on-majority** (new resolver variant) | start-active or reachable via reform | Roman *comitia centuriata*; Solon |
| DELIBERATIVE_ASSEMBLY | Agôn (mass) fed by a sortition-FLAG roster; Inquiry/ProofBar as retroactive legality Chain Contest | **latent/emergent only** (needs a charter breaking oligarchy) | Athens Ekklesia+Boule+kleroterion+graphē paranomōn |
| CONSENSUS_UNANIMITY | Consensus mode (roster + Holdout clock + frivolous-block antibody; **add a 3rd assent/stand-aside/holdout state**) | start-active for clan/tribal/religious factions | Haudenosaunee; Quaker; Gadaa; *shūrā* |
| NEGOTIATED_ESTATES | Negotiation (BATNA/ZOPA/offer-table; **+ mechanically-enforced win-set for bound-mandate delegates**) | start-active at Country/Duchy | Cortes of León; Estates-General; guild charters |
| MERITOCRATIC_BUREAUCRATIC | Inquiry-as-composition (examiner/quota) → Directive posting, **+ anti-capture "no home-province posting"** | latent (blocked on Crown Administrative pipeline ED-FA-0018) | Chinese examination + Law of Avoidance |

**Standout additions:**
- **NEW propagation shape "elect-inward, account-back"** (Venice Great Council → Senate → Ten): a body spins
  off a *narrower, time-boxed, more-empowered* committee accountable back to its **same-tier** creator —
  distinct from top-down cascade and bottom-up aggregation; recommend adding to `governance_type_registry §4`
  alongside propagation/dissemination/accumulation/dissipation. (Different from game_precedents G6 CK3-Council:
  power flows from a *peer body's delegation*, not a superior's fiat, and must be returned.)
- **Consensus 3-state** (assent / **stand-aside** / holdout), from Quaker practice — a graceful non-blocking dissent.
- **Liberum veto** = the negative control: Consensus with the antibody *removed* → a Crisis-card trigger, not a mode.
- **Solon→Cleisthenes** = a real historical **mode-flip driven by crisis+reform** (grounds "governance mode can change, path-dependent"; the non-videogame twin of game_precedents G4).
- **Law of Avoidance** (no posting to one's home province) = a cheap anti-capture FLAG; grounds the open ED-FA-0018.

---

## B · Caste, franchise & intrapopulation conflict (→ GAP-F1..F5, GAP-F3 circumvention)

**Caste (grounds `faction_politics_v30` Part 3):** Valoria's Einhir split is structurally **jati-like**
(endogamy + occupational/institutional closure), not clean four-fold *varna*. Genuinely-new nuances the
corpus lacks:
- **Regional inconsistency** — the same caste can rank differently by region (jati); Valoria's caste is realm-uniform.
- **Reversible judicial demotion tier** (Japanese *hinin* vs fixed *eta*) — a demote-with-recovery-path the binary birth-caste model lacks (grades §3.6's caste-transgressive Conviction).
- **Coexisting closed-birth + open-wealth axes** (Roman patrician/plebeian *and* equestrian/senatorial) — Valoria's caste is single-axis; no raw-wealth bypass exists.
- ***limpieza de sangre*** = the closest total-system analog (post-conflict, ancestry-based, religious-institutional, investigation-based, **gameable** — forged/purchased proof was normal). Temporal cross-scale (genealogy back in time), matching Conviction-Scar accumulation.

**Caste circumvention (GAP-F3) — corpus has only sponsorship-Disposition-burn; history adds three:**
**wealth-buyout** (Solon/equestrian threshold), **forged/purchased proof** (*limpieza* — hang on the
existing Conviction-Scar/exposure machinery), **group-scale cultural reclassification** (*sanskritization*
— a settlement/territory-scale, multi-season process → the natural home for `franchise_v30 §5.1`'s open
"Caste reform event (TBD)" hook, **not** the PC-scale mechanic). *devshirme* + *novus homo* = confirmations
of already-built mechanics (Riskbreakers/Niflhel favoring outsiders; §3.5 persistent Disposition floors) —
citation-patches, not new design.

**Franchise (grounds `franchise_v30`):** territory-as-the-unit-of-weight is **historically well-founded**
(medieval guild/borough charter holds the franchise, not the person; Roman century is the counting unit,
not the citizen). Periodic ±1 reapportionment (not binary suffrage on/off) matches how weighted-bloc systems
really evolved (241 BCE *comitia* reform ≈ §5.1 Shift Triggers). **Warning:** liberalizing one exclusion
axis can **harden another** (US 1820s–30s: property bars fell as racial bars rose) — a Franchise-reform
event may need an explicit "displaced-exclusion" side-effect, not a clean +1. Landholder *direct* democracy
(Landsgemeinde/*popolo*) = a **cautionary** case (re-concentrated into signorial rule) — argues *for*
keeping Franchise weighted/corporate, against flattening.

**Intrapopulation conflict / the fracturing engine (GAP-F4/F5) — the missing resolution registers:**
- **Millet-fission = a peaceful "recognition fission" insurgency-FORMATION path** — charter a new sub-faction
  out of a permanently-diverged population instead of fighting/ignoring it. `insurgency_pipeline §4.1` has
  **one** formation trigger (territorial neglect) and no negotiated-recognition path. **Highest-value single add.**
- **Cleisthenes "reaggregation" = a genuinely NEW 4th resolution category** (beyond concession/suppression/
  power-sharing): change *how* allegiance aggregates (redraw the blocs) rather than the values — a Crown action
  that dilutes a regional bloc structurally. Nothing in the current stack touches aggregation *topology*.
- ***secessio plebis*** = organized **non-violent withdrawal-as-leverage**, a pressure lever *between* unrest and
  full Insurgency — unmodeled.
- ***hetaireiai*** (Greek elite clubs) = an **informal cross-household/cross-faction network beneath the formal
  rank ladder** — unmodeled (the Inner Circle mechanic is formal/per-faction).
- **Dorr Rebellion** = a 5th dissolution flavor: **"failure of nerve" collapse** (a promoted authority never
  consolidates control it nominally holds) — distinct from the RAND 4 paths.
- **Ciompi** = **post-recognition reversal by domestic counter-coup** — a case-type the RAND-grounded 4-path
  dissolution model (about *pre*-recognition insurgencies) doesn't cleanly cover; bears on the open
  `INSURGENCY-DEMOTE-DIRECTION-001` flag.
- **Peasant-revolt comparison** (England 1381 vs Germany 1524) → a **"Concession Residue"** sub-flag on the
  military-defeat path (quiet policy absorption vs none) — a narrow refinement.
- **Machiavelli's two humors** confirm the parliamentary-vent asymmetry (`insurgency_pipeline §5.2`) is sound,
  and argue for eventually allowing an extra-parliamentary faction a path *into* the vented condition (a
  permanently-unvented humor is a chronic destabilizer) — directly bears on INSURGENCY-DEMOTE-DIRECTION-001.
- **SURFACE-ANALOGY WARNING:** Byzantine **Blues/Greens** were caste/class-*orthogonal* — REAL for cross-caste
  coalition-formation, a **misuse** if folded into the caste thread. Medieval three-orders + Landsgemeinde =
  prose/flavor only, no mechanic.
- **Namespace-collision flag:** the settlement generator's "P11/P2" (allegiance vs owner) collides with
  `canon` P-11/P-02 (threadwork metaphysics) — flag to whoever owns `governance_type_registry`.

---

## C · Religious/cultural orthodoxy, heresy & suppression (→ GAP-G1, GAP-G2)

**Conceptual spine:** heresy (willful, corrected-and-persisted deviation *inside* the fold) ≠ non-orthodoxy/
paganism (*outside* the fold from the start). Different tools: the millet/dhimmi apparatus is a
**jurisdictional membrane** around never-insiders; the Inquisition is a **disciplinary procedure** for people
the institution insists it still owns. PT (Piety Track) models only the single insider axis — **no separate
non-orthodox/minority-accommodation channel** (millet/dhimmi) exists (a real gap).

**Suppression backfires by SEVEN distinct, nameable mechanisms** (a design-honest formalization — a fix must
name which it risks):
1. **Resource/Treasury** (skilled-population flight is a self-inflicted wound) — Huguenot exodus; 1492/1609 expulsions.
2. **Legitimacy-contagion** (reputational hit with third parties never touched) — Magdeburg/Rome sack (FA-6); Revocation.
3. **Quiet trust-decay** (corrodes the target's internal cooperation for generations, *no revolt, no trigger*) — PNAS Inquisition study → argues for **ambient Church-Attention-Pool trust decay independent of any verdict** (unmodeled).
4. **Identity-hardening / non-reintegration** — Chalcedonian schism; kakure/hanare kirishitan.
5. **Identity-migration** (severe suppression converts a **militarily-solvable** problem into a **militarily-unsolvable** one) — Rome vs Jerusalem: the harshest option should risk handing the problem from Conquest/mass-battle to **Fieldwork/Investigation**. *Most novel finding.*
6. **Sponsor/insurgency** — Reformation, Camisards, Cathars → **couple Reformation-schism survival to the Insurgency Pipeline's existing sponsor mechanic (ED-881), don't re-derive**.
7. **No-off-ramp ratchet** — a track keyed to something *uncorrectable* (ancestry, *limpieza*) has no negotiated exit and **must escalate to expulsion**; a *belief* track must keep its Acquittal/recant off-ramp genuinely reachable.

**Counterweight (keeps it non-moralizing):** toleration is **not free** — it's the lower-variance,
**deferred-cost** option whose bill comes due at moments of central weakness (Ottoman millet → 19th-c
nationalism). Build the accommodation lever as a variance/timing trade, not a good/evil dial — reuse **FA-8
Protected-Tributary's shape** (dhimmi/jizya convergence).

**Other REAL mechanisms:**
- **Axis-capture** — a suppression apparatus (CI/PT/Heresy Investigation) is a **resource rivals weaponize for
  unrelated ends**: Albigensian Crusade = heresy-suppression as a *cover* for Capetian annexation (composes with
  the Storm/Sack + "Impose Administration" fork); Byzantine iconoclasm = a Crown land-grab from monasteries.
  Model capture-vulnerability **generally**, as a feature to model, not a corruption to prevent.
- **Investiture Controversy → Concordat of Worms** = a **collision-resolution SHAPE**: split a contested
  CI-vs-Mandate resource into **two non-competing channels** (extends the T7 advowson finding) rather than a
  winner-take-all roll.
- **Interdict** = a **collective/territory-grain sanction** (vs the single-target Excommunication Tribunal), with
  a built-in backfire (resentment against the clergy) — a missing, well-precedented action.
- **Ecumenical councils** = the direct ancestor of the Heresy-Investigation Verdict phase (define-by-vote + anathematize).
- **Auto-da-fé** = a distinct **public-Verdict performance layer** (projects onto every NPC present), separate from adjudication.
- **Doctrinal drift** on long-suppressed Latent identities (kakure/hanare) — restored toleration doesn't fully
  satisfy the original grievance after many seasons underground → a schism-on-reemergence outcome.
- **SURFACE-ANALOGY WARNING:** Rome vs **Carthage** — "total erasure achieved" is **historically false** (Neo-Punic
  persisted ~500 yrs — inscriptions to ~3rd c. CE, spoken to Augustine, d. 430; the "salted earth" detail is apocryphal). Any mechanic implying a suppression/conquest can
  *fully zero* a Conviction/identity track should be **rejected — model a floor, not a zero.**
