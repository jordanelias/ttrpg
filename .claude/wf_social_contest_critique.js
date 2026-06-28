export const meta = {
  name: 'social-contest-deliberation-critique',
  description: 'Critique the Valoria social contest system against the deliberation/politics-as-game research corpus (4 senses of game, Caillois families, commitment stores, mechanism design, the meta-game). One analyst per theoretical lens; each finding adversarially verified against the actual system files (checking whether claimed gaps are filled elsewhere).',
  phases: [
    { title: 'Critique', detail: '8 parallel analysts, one per theoretical lens, hold the system against the research and surface strengths + under/mis-configurations with verbatim quotes' },
    { title: 'Verify', detail: 'each finding adversarially re-checked: is the critique sound, and is the claimed gap actually unfilled across the whole corpus?' },
  ],
}

const CORPUS = [
  'VALORIA SOCIAL CONTEST CORPUS (repo-relative, cwd = C:/Github/ttrpg). Read what your lens needs:',
  '  PRIMARY (the system under critique):',
  '  designs/scene/social_contest_v30.md          - main spec, sections 1-12 (setup, exchange, resolution, asymmetric, BG, hybrid, obligations, succession, heresy).',
  '  designs/scene/social_contest_v30_infill.md   - prose/rationale infill.',
  '  params/contest.md                            - formulas, tables, patch log.',
  '  params/contest_extensions.md                 - Resonant Style targeting, Evidence Findings, temporal-axis, etc.',
  '  sim/personal/contest.py                      - Python sim of the contest pipeline.',
  '  ADJACENT (the systems the contest plugs into - GREP THESE before claiming a gap is unfilled):',
  '  designs/npcs/npc_behavior_v30.md             - Stance Triangle, Conviction, Resonant Style taxonomy (S1.3), Conviction Scars (S3.3/3.4), arcs.',
  '  designs/personal/conviction_taxonomy_v30.md  - the 13-Conviction / 4-axis matrix (the interpretation primitive).',
  '  designs/personal/knots_v30.md                - Knot/Disposition (-5..+5) relational substrate.',
  '  designs/architecture/*                        - key_substrate, scale_transitions, complete_systems_reference (the Key bus, armature dot-product).',
  '  references/module_contracts.yaml             - module boundaries, resolver classes.',
  '  designs/audit/2026-06-28-distillation-coherence/distillation_coherence_report.md - recent engine audit: "two primitives" (sigma resolver + armature dot-product), the contest IS the sigma kernel.',
].join('\n')

const PHILOSOPHY = [
  'DESIGN PHILOSOPHY (the standard to judge against - this is what "well-configured" means here):',
  '  - GRANULAR, BOTTOM-UP EMERGENT with TOP-DOWN VALIDATION. Macro outcomes (who wins, who governs,',
  '    what becomes binding) should EMERGE from granular per-move substrate, validated by a top-down constraint',
  '    (the adjudicator / persuasion track / obligation). Hard-coded macro outcomes are a smell.',
  '  - WORLD/PLAYER CHURN AXIOM: every decision must generate churn that seeds emergent narrative. SUSPECT any',
  '    inert or unreachable mechanic. A procedure whose FAILURE MODES generate story (capture, holdout, the',
  '    antechamber maneuver) is high-value churn, not a bug.',
  '  - ENGINE DISCIPLINE: there are two universal primitives - the SIGMA RESOLVER (will+advantage -> outcome) and',
  '    the ARMATURE DOT-PRODUCT (event -> meaning-for-an-observer, over a 13-Conviction x 4-axis matrix). A good',
  '    improvement REUSES these primitives and the Key bus; it does not bolt on a parallel subsystem.',
  '  Judge the contest as a DELIBERATIVE GAME in the rigorous sense, not just for internal consistency.',
].join('\n')

const METHOD = [
  'METHOD:',
  '  For your lens, do THREE things, honestly:',
  '   (1) CREDIT what the system already gets right against the research (cite it - strengths keep the critique honest).',
  '   (2) Find UNDER-CONFIGURATION (the research shows a richer design space the system has collapsed or omitted).',
  '   (3) Find MIS-CONFIGURATION (the system is configured in a way that FIGHTS the philosophy above - e.g. hard-codes',
  '       what should emerge, or suppresses churn the research says is the point).',
  '  EVIDENCE RULE: every claim about the system MUST carry a SHORT VERBATIM QUOTE you actually read from a named file.',
  '  Before asserting "X is missing", GREP THE ADJACENT FILES - the corpus is large and a mechanic may live in',
  '  npc_behavior / conviction_taxonomy / knots / faction docs. If it exists elsewhere, say so and downgrade to a',
  '  seam/integration finding rather than an absence.',
  '  Every improvement must be CONCRETE and reuse the engine primitives (sigma resolver, armature dot-product, Key bus,',
  '  the existing track/clock/pool buckets) where possible. No "add a whole new subsystem" hand-waving.',
].join('\n')

const LENSES = [
  {
    key: 'four-games',
    title: 'One track for four different games',
    brief: [
      'RESEARCH: The deliberation synthesis (Part 0) shows "game" is FOUR non-coextensive senses: Wittgensteinian',
      '(rule-constituted), Suitsian (voluntary inefficient obstacles), AGONISTIC (zero-sum contest with a victor),',
      'and GAME-THEORETIC (strategic interdependence, often MIXED-MOTIVE / positive-sum). Its deepest finding (Part VI.2-3,',
      'pragma-dialectics): the healthiest deliberation is resolution-ON-THE-MERITS, and "trying to win at all costs" is the',
      'very disposition that PRODUCES fallacies; eristic (pure contest) is the DEGENERATE type. The politics companion (Part D.4)',
      'sharpens it: the one word "game" quietly holds together FOUR different things a procedure can do - PRODUCE A WINNER,',
      'STRIKE A BARGAIN (positive-sum), DISCERN A TRUTH, or ENACT A UNITY - and the interesting questions live in the gaps.',
      '',
      'CRITIQUE TASK: The Valoria contest resolves almost everything on ONE bidirectional zero-sum Persuasion Track (0-10,',
      'Side A wins >=7 / Side B wins <=3, strain-as-damage, Composure-as-hit-points). Examine whether this collapses the four',
      'games into one agonistic bar. Look hard at: the Compromise zone (4-6) - is it a genuine positive-sum BARGAIN or just a',
      '"nobody won" default? (note S12 explicitly DEFERS "Negotiation compromise resolution (ZOPA-style)... structurally',
      'different from Persuasion Track, not designed"). Does anything reward resolution-on-the-merits vs win-at-all-costs?',
      'Is "discern a truth" (inquiry) modeled at all, or only persuasion/victory? Assess whether the single-track design is the',
      'right unification or a flattening that destroys churn the four-way distinction would generate.',
    ].join('\n'),
  },
  {
    key: 'commitment-store',
    title: 'No commitment store - hit-points, not concessions',
    brief: [
      'RESEARCH: The deepest, least-disputable correspondence (deliberation Part II.B-D, Part V.5): real argument is a',
      'MOVE-AND-COMMITMENT structure with a COMMITMENT STORE (Hamblin) - a running ledger of the propositions each party has',
      'conceded, which legal moves (assert, question, challenge, concede, justify) ALTER. Walton-Krabbe build six dialogue types',
      'on it; Dutilh Novaes shows even solitary deduction is an internalized Prover-Skeptic exchange. Validity/truth are DEFINED',
      'as having a winning STRATEGY over this structure. The commitment store is the granular substrate from which argumentative',
      'macro-structure emerges - i.e. it is the BOTTOM-UP substrate this project says it wants.',
      '',
      'CRITIQUE TASK: Does the Valoria contest have any commitment store? Examine what actually persists across exchanges: the',
      'Persuasion Track (a scalar), Doubt Markers (one transient -2), Recall "+2D when citing a specific named verifiable claim"',
      '(binary, per-exchange/per-source), Concentration, strain. Argument CONTENT (genre/orientation/style) buys dice bonuses but',
      'is there any persistent LEDGER of what each side has conceded or committed to, that constrains later moves? Is a contest a',
      'sequence of dice-margin attacks on a hit-point bar, or a structured exchange of commitments? Assess this as the single',
      'biggest bottom-up-substrate question. If a partial ledger exists (Obligations are post-contest; Beliefs/Convictions are',
      'NPC-side), say precisely how far it falls short of an IN-CONTEST commitment store. Propose how a commitment store could be',
      'a track/clock substrate the sigma resolver reads (reusing the engine), not a bolt-on.',
    ].join('\n'),
  },
  {
    key: 'caillois-families',
    title: 'One Caillois family (pure agon) - no alea / mimicry / ilinx',
    brief: [
      'RESEARCH: The politics companion classifies decision-procedures by Caillois\'s four families - AGON (regulated merit',
      'contest), ALEA (chance/lot), MIMICRY (performed legitimacy - acclamation, quasi-inspiration, sovereignty-as-performance),',
      'ILINX (the crowd-roar, charismatic/sacral charge). Pre-1600 polities mixed them: sortition (alea) to KILL FACTION by',
      'removing the prize; acclamation/quasi-inspiration (mimicry) as a real resolution mode (canonical Church election had THREE',
      'modes: scrutiny=agon, compromise=delegated agon, quasi-inspiration=mimicry); the Venetian doge = engineered ALEA+AGON',
      'hybrid to defeat capture. Succession was alea (primogeniture), agon (tanistry/kurultai), OR mimicry (acclamation).',
      '',
      'CRITIQUE TASK: The Valoria contest appears to be PURE AGON (dice-pool merit contest -> victor). Verify across the corpus',
      '(GREP for sortition/lot/acclamation/random) whether ANY non-agon resolution family exists. In particular: the Succession',
      'Contest (S7.2) uses Grand Contest infrastructure = pure agon, where history/theory show succession is often alea or mimicry.',
      'Is there any lot/sortition mechanic anywhere (an anti-capture, anti-faction device)? Any acclamation/quasi-inspiration',
      'resolution? Is ilinx (crowd affect) present beyond Charisma-as-pool? Assess whether having ONE resolution family where the',
      'research shows at least four - each generating DIFFERENT churn - is an under-configuration. Propose concrete additions that',
      'reuse the engine (e.g. an alea-hybrid succession; acclamation as a mimicry resolution mode).',
    ].join('\n'),
  },
  {
    key: 'contest-locus-and-type3',
    title: 'Where the contest sits + missing Type-3 pathology churn',
    brief: [
      'RESEARCH: The politics companion (Part D.1) - the load-bearing distinction is WHERE THE COMPETITION SITS relative to the',
      'decision: TYPE 1 (the contest IS the deciding: council/assembly/combat/adjudication), TYPE 2 (selects WHO decides:',
      'election, succession, degenerate-fiat), TYPE 3 (REMOVES competition by design: sortition, consensus). The crucial finding:',
      'Type-3 procedures generate their characteristic PATHOLOGY - the abolished competition RE-EMERGES (the consensus holdout/veto;',
      'the captured lottery pool; the liberum veto paralyzing the state). That re-emergence IS emergent narrative. Constitutions',
      'build "anti-gaming" antibodies (the Iroquois anti-frivolous-objection rule; Venetian anti-bribery oaths) precisely because',
      'they know the procedure can be gamed.',
      '',
      'CRITIQUE TASK: Map Valoria\'s contest types onto Type 1/2/3. It clearly has Type 1 (Formal/Grand Contest) and a Type 2',
      '(Succession Contest, election-by-electors-style). Does it have ANY Type 3 (consensus/unanimity, or sortition)? More important',
      'for the churn axiom: does the system model PROCEDURAL PATHOLOGY as a story engine - the holdout, the deadlock-gamed-for-leverage,',
      'the captured pool? It has Deadlock/Chain rules (S6.3) and Stays - assess whether these EXHAUST the design (they look like',
      'TERMINATORS that resolve stalls, the opposite of treating the pathology as generative churn). Connect directly to the churn',
      'axiom: the richest churn is a procedure whose failure mode seeds the next arc, and Valoria may be configured to suppress',
      'exactly that. Propose Type-3 procedures and pathology-as-churn hooks.',
    ].join('\n'),
  },
  {
    key: 'meta-game-capture',
    title: 'The meta-game: procedure capture, robust action, the broglio, the antechamber',
    brief: [
      'RESEARCH (the richest churn lens): The machination + testing companions show the CENTRAL empirical finding of the whole',
      'corpus - the SAME procedural materials produce wildly different outcomes by MECHANISM DESIGN and by CAPTURE. The Medici did',
      'NOT abolish Florence\'s lottery; they CAPTURED it (loaded the pool via accoppiatori/Borsellino, bypassed the draw "a mano").',
      'Cosimo won by ROBUST ACTION + MULTIVOCALITY (noncommittal moves preserving his options while narrowing opponents\'; one',
      'action legible from many angles). Venice did not eliminate maneuver; it CHANNELED it - the broglio: electioneering on the',
      'stairways, "big fish eat the smaller", the Signoria "helpless to stop the lobbying". Fiat DISPLACES contest to the',
      'ANTECHAMBER ("the most absolutist polities generate the most baroque court politics"). And politics Part D.4 + Hart\'s rule',
      'of recognition: the deepest political act is CHOOSING WHICH GAME legitimates power - a META-GAME.',
      '',
      'CRITIQUE TASK: Valoria\'s contest treats THE RULES AS FIXED AND FAIR - the GM sets adjudicator type, exchange count,',
      'resistance, faction boost at setup (S2), and play happens inside fixed rules. Examine: (a) Can a faction CAPTURE the',
      'procedure itself - load the pool, capture the adjudicator, choose the venue/adjudicator-type to its advantage? (BG Lobbying',
      'and the Lobby Cap S10/PP-256 are the closest - assess whether they model capture or just a +/-2 nudge.) (b) Is there any',
      'ROBUST-ACTION / multivocality lever (committing-legibly vs staying-ambiguous as a strategic choice)? (c) Is there an',
      'ANTECHAMBER / broglio layer - off-table maneuver, vote-soliciting, the channeled-not-eliminated game - or does all social',
      'conflict route through the formal contest? (d) Is the CHOICE OF PROCEDURE a player-facing, contestable, churn-generating',
      'lever, or hard-coded at GM setup? This is likely the highest-leverage region for improvement given the churn axiom. Propose',
      'concrete capture/robust-action/antechamber mechanics that reuse faction state, Disposition, and the Key bus.',
    ].join('\n'),
  },
  {
    key: 'adjudicator-armature',
    title: 'Adjudicator as a resistance scalar, not an armature/agent',
    brief: [
      'RESEARCH: The adjudicator is the firmest cross-domain correspondence (deliberation Part III.D, V.8): an impartial',
      'rule-applier who DECLARES the outcome - and Aristotle (Part I.G) grounds the three oratory genera in three KINDS of judge',
      '(juror of the past, juror of the future, spectator who judges the speaker). Competitive debate\'s tabula-rasa paradigm: judge',
      'decides solely on arguments made in the round. Politics model 9: the count was construed as DISCERNING the sanior et maior',
      'pars ("sounder and greater part"), and the LOSER could claim to BE the sounder part - discernment-language weaponized inside',
      'the dispute. I.e. the adjudicator is an AGENT with a standard the arguments must satisfy, not a number.',
      '',
      'CRITIQUE TASK: Valoria\'s adjudicator types (Expert Judge/Crowd/No-adjudicator/Panel, S2-S3) cleverly select the PRIMARY',
      'ATTRIBUTE (Cognition/Charisma/Attunement) - CREDIT this, it maps Aristotle\'s three judges well. BUT examine: beyond picking',
      'the attribute and contributing a "resistance" number (avg faction Stability -1) and a single faction "boost", does the',
      'adjudicator DELIBERATE? Does it have its own armature/convictions the argument must satisfy (the engine HAS a 13-Conviction',
      'x 4-axis armature dot-product - is the adjudicator one)? Is "Panel" still undesigned (ED-137)? Is there any sanior-pars',
      'dynamic (a losing side contesting the legitimacy of the verdict)? Assess whether the adjudicator is under-configured as a',
      'flat resistance scalar when the engine already has the primitive to make adjudication EMERGENT (argument symbolic-dimensions',
      'dot-producted against the adjudicator armature). Propose reusing the armature dot-product for adjudication.',
    ].join('\n'),
  },
  {
    key: 'fallacies-as-fouls',
    title: 'No fallacies-as-fouls, no dialectical shift, no good-faith/eristic distinction',
    brief: [
      'RESEARCH: Pragma-dialectics (deliberation Part II.C, V.10) defines a fallacy AS the violation of a discussion rule - a FOUL,',
      'an illegitimate move penalized within the game; the ten rules function as constitutive rules. Walton-Krabbe: a DIALECTICAL',
      'SHIFT (the exchange changing type mid-stream - a negotiation move smuggled into an inquiry) is productive when noticed and a',
      'source of fallacy/bad-faith when not. And the cooperative/competitive fault line (Part VI.2): the activity is healthiest when',
      'participants treat it LEAST as a contest to win; eristic is the degenerate type.',
      '',
      'CRITIQUE TASK: Valoria penalizes PHYSICAL fouls (S9.6 Chamber Violence = immediate forfeit) - CREDIT that. But examine',
      'whether there is any ARGUMENTATIVE foul system: a penalty for an illegitimate argumentative move, a bad-faith genre/style',
      'switch, an unmarked dialectical shift, eristic for its own sake. Is there any mechanic distinguishing good-faith',
      'resolution-seeking from win-at-all-costs? (Note the "Obscuring" orientation and "Suppression/Insinuation" styles - are these',
      'modeled as legitimate-but-shady tactics with consequences, or just neutral dice options?) The Adjudicator Thread Response',
      'table (S9.4b) penalizes one specific foul (illicit Thread use) - assess whether that is the ONLY foul concept and whether a',
      'general fouls-as-fouls layer is missing. Connect to churn: a foul caught/uncaught is a story. Propose a foul mechanic reusing',
      'the adjudicator and Doubt-Marker machinery.',
    ].join('\n'),
  },
  {
    key: 'mixed-motive-bargain',
    title: 'Mixed-motive bargaining, two-level games, and escalation between modes',
    brief: [
      'RESEARCH: Negotiation (deliberation Part IV) is the strictest game-theoretic game AND precisely NOT a zero-sum contest -',
      'it is MIXED-MOTIVE (parties cooperate to create the surplus, compete over its division: integrative vs distributive,',
      'Walton-McKersie; Nash bargain; ZOPA). Putnam\'s TWO-LEVEL game: a negotiator plays two boards at once (the table + domestic',
      'ratification), bound by a WIN-SET; a move strengthening one table can lose the other. Parliaments (politics model 8) are',
      'SUPPLY-FOR-REDRESS bargains, not pure contests. Litigation (deliberation III.E, Priest-Klein): cases SELECT for trial',
      'precisely when closest - i.e. a good system should route lopsided disputes AWAY from full contest.',
      '',
      'CRITIQUE TASK: Examine Valoria\'s treatment of bargaining. S12 explicitly DEFERS "Negotiation compromise resolution',
      '(ZOPA-style)" AND "Escalation between social modes (negotiation->debate->appeal)". The BG Parliamentary Vote (S10) and Hybrid',
      '(S11) and "Private Negotiation" proceeding type all still resolve on the same zero-sum Persuasion Track. Is parliament modeled',
      'as a supply-for-redress BARGAIN (each side can gain) or as a vote-contest (one side wins)? Is the Lead orator in a coalition',
      'mechanically ANSWERABLE to a faction win-set (Putnam two-level), or is the coalition just a shared dice/Concentration pool',
      '(S9.2)? Is there a "this dispute is too lopsided for a full contest" gate (Priest-Klein selection)? Note S1: "GMs should not',
      'call for a contest when one side has no plausible case" - is that the only selection mechanism? Assess the mixed-motive gap',
      'and propose a ZOPA/win-set treatment that reuses Disposition/faction-stat deltas as the bargaining payoffs.',
    ].join('\n'),
  },
]

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    summary: { type: 'string', description: 'one-paragraph verdict for this lens: how well-configured is the system on this dimension?' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'short stable id, e.g. FG-1' },
          type: { type: 'string', enum: ['strength', 'under-configured', 'mis-configured'] },
          title: { type: 'string' },
          research_basis: { type: 'string', description: 'the concept + source from the research corpus that grounds this' },
          system_state: { type: 'string', description: 'what the system currently does, in one or two sentences' },
          locations: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                file: { type: 'string' },
                section: { type: 'string' },
                quote: { type: 'string', description: 'verbatim text actually read from the file' },
              },
              required: ['file', 'quote'],
            },
          },
          critique: { type: 'string', description: 'the precise gap/misconfig, or for a strength, why it maps well' },
          churn_relevance: { type: 'string', description: 'how this bears on bottom-up-emergent + the churn axiom' },
          improvement: { type: 'string', description: 'concrete region for improvement, reusing engine primitives where possible. Empty for pure strengths.' },
          leverage: { type: 'string', enum: ['high', 'medium', 'low'] },
          effort: { type: 'string', enum: ['low', 'medium', 'high'] },
        },
        required: ['id', 'type', 'title', 'research_basis', 'system_state', 'locations', 'critique', 'churn_relevance', 'leverage'],
      },
    },
  },
  required: ['lens', 'summary', 'findings'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    finding_id: { type: 'string' },
    verdict: { type: 'string', enum: ['sound', 'already-handled', 'overstated', 'refuted', 'uncertain'] },
    reasoning: { type: 'string', description: 'why. If already-handled, name WHERE in the corpus the mechanic actually lives, with a quote.' },
    evidence_quote: { type: 'string', description: 'a key verbatim quote you independently located (esp. checking whether a claimed gap is filled elsewhere)' },
    corrected_leverage: { type: 'string', enum: ['high', 'medium', 'low'] },
    refined_improvement: { type: 'string', description: 'tighten or correct the proposed improvement if needed' },
  },
  required: ['finding_id', 'verdict', 'reasoning'],
}

phase('Critique')
const results = await pipeline(
  LENSES,
  (l) => agent(
    [
      'You are a senior game-systems designer and philosopher of deliberation, critiquing the Valoria TTRPG social contest system.',
      'You have deep command of the research corpus (deliberation-as-game; politics-as-deliberative-game; Renaissance machination & mechanism design).',
      'Your lens: ' + l.title + '.',
      '',
      CORPUS, '', PHILOSOPHY, '', METHOD,
      '',
      'YOUR LENS BRIEF:', l.brief,
      '',
      'Return findings in the schema. lens="' + l.key + '". Aim for the 3-6 SHARPEST findings (mix of strengths and gaps), each grounded in a verbatim quote. Quality over quantity. Do not invent gaps without grepping the adjacent files first.',
    ].join('\n'),
    { label: 'critique:' + l.key, phase: 'Critique', schema: FINDINGS_SCHEMA, effort: 'high' },
  ),
  (review, l) => {
    const findings = (review && review.findings) ? review.findings : []
    return parallel(findings.map((f) => () =>
      agent(
        [
          'ADVERSARIAL VERIFICATION of a design-critique finding about the Valoria social contest system.',
          'Your job: pressure-test it. Open the cited files AND grep the adjacent corpus yourself.',
          CORPUS,
          '',
          'FINDING (JSON):', JSON.stringify(f, null, 2),
          '',
          'Decide a verdict:',
          ' - "sound": the critique holds; the gap/strength is real as described.',
          ' - "already-handled": the claimed gap is actually addressed somewhere in the corpus (npc_behavior, conviction_taxonomy, knots, faction docs, etc.). NAME WHERE with a quote. This is the most important check - the corpus is large.',
          ' - "overstated": partly true but the severity/leverage is too high, or the system handles more of it than claimed.',
          ' - "refuted": a cited quote cannot be located, or is out of context such that the critique does not hold.',
          ' - "uncertain": cannot resolve from the files.',
          'Independently locate at least one evidence_quote. Assess corrected_leverage honestly. Tighten the improvement if the original is vague or would violate engine discipline (no bolt-on subsystems; reuse sigma resolver / armature dot-product / Key bus).',
          'Return the verdict schema. finding_id = "' + f.id + '".',
        ].join('\n'),
        { label: 'verify:' + l.key + ':' + f.id, phase: 'Verify', schema: VERDICT_SCHEMA, effort: 'high' },
      ).then((v) => Object.assign({}, f, { lens: l.key, verdict: v })).catch(() => null),
    ))
  },
)

const all = results.flat().filter(Boolean)
const lensSummaries = results.map((r, i) => ({ lens: LENSES[i].key, title: LENSES[i].title })) // placeholder; summaries returned per-lens below
const sound = all.filter((f) => f.verdict && (f.verdict.verdict === 'sound' || f.verdict.verdict === 'overstated' || f.verdict.verdict === 'already-handled'))
const refuted = all.filter((f) => f.verdict && f.verdict.verdict === 'refuted')
const strengths = all.filter((f) => f.type === 'strength' && f.verdict && f.verdict.verdict !== 'refuted')
const gaps = all.filter((f) => f.type !== 'strength' && f.verdict && (f.verdict.verdict === 'sound' || f.verdict.verdict === 'overstated' || f.verdict.verdict === 'already-handled'))

log('critique complete: ' + all.length + ' findings raised; ' + gaps.length + ' gaps survive, ' + strengths.length + ' strengths, ' + refuted.length + ' refuted')

return {
  totals: { raised: all.length, gaps: gaps.length, strengths: strengths.length, refuted: refuted.length },
  gaps,
  strengths,
  refuted,
  uncertain: all.filter((f) => f.verdict && f.verdict.verdict === 'uncertain'),
}
