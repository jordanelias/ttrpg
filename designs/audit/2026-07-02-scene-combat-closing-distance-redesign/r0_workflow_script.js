export const meta = {
  name: 'r0-closing-distance-research',
  description: 'R0: HEMA/treatise grounding research for the closing-distance/facing/grip subsystem redesign',
  phases: [
    { title: 'Research', detail: '4 clusters ground facts from HEMA/treatise sources', model: 'sonnet' },
    { title: 'Synthesize', detail: 'cross-cluster consistency + a single combined brief', model: 'opus' },
  ],
}

var SCRATCH = 'C:/Users/Jordan/AppData/Local/Temp/claude/C--Github-ttrpg/8445ad5a-bbe0-408b-9e76-179d73e745ef/scratchpad'
var OUT = SCRATCH + '/r0'
var ENG = 'C:/Github/ttrpg-morph-rearch/designs/scene/combat_engine_v1'

var DISCIPLINE = [
  'PURPOSE: Valoria\'s scene-combat engine currently under-models how a shorter-reach fighter closes distance',
  'against a longer weapon (spear/polearm-class weapons win 84-96% of matchups against an arming sword in the',
  'CURRENT engine, and Jordan has confirmed this needs a genuine mechanics redesign, not just number-tuning).',
  'Read ' + ENG + '/wrapper.py (the engagement() function is the state machine — approach phase from line ~85,',
  'closed-exchange from ~110) and ' + ENG + '/systems.py (reach_base, close_rate, approach_displace, leverage,',
  'commit_depth, recoverability_factor, at_grip, grip_target) to see EXACTLY what already exists before',
  'researching what to ADD — do not propose a mechanic that already exists under a different name.',
  '',
  'YOUR JOB: ground PHYSICAL, ATTESTABLE FACTS from HEMA treatises and martial-arts biomechanics — the SAME',
  'discipline the project\'s prior morphology research used: facts only, no fiat effectiveness numbers, no',
  'invented 0-1 scalars. The test for every claim: is it something a treatise explicitly describes, or a',
  'biomechanically measurable fact (a joint-extension distance, a documented technique name, a described',
  'footwork pattern), not your own guess at "how effective" something should be. Cite the specific source',
  '(author, treatise, folio/section where possible) for every technique or claim. Where sources disagree or a',
  'claim is uncertain, say so explicitly rather than picking one silently.',
  '',
  'OUTPUT: write ONE valid JSON file (no markdown fences) to the path given below, structured as facts with',
  'citations — NOT a design proposal (do not suggest formulas, gains, or 0-1 scalars; that is a LATER phase\'s',
  'job). Your final MESSAGE must be short: 3-5 sentences on the strongest-grounded findings.',
].join('\n')

var CLUSTERS = [
  { key: 'measure_gap',
    prompt: 'Research how a SHORTER/closer fighter manages measure against a LONGER weapon (spear, polearm, ' +
      'longer sword) historically, and how the longer weapon tries to deny that closing. Cover: ' +
      '(1) documented footwork patterns for closing distance safely against a thrusting weapon (voiding the ' +
      'line, angling off, gathering steps vs passing steps) -- Fiore dei Liberi (Fior di Battaglia, spear/' +
      'polearm plays), Meyer (Kunst des Fechtens, langes Schwert vs stange), George Silver (Paradoxes of ' +
      'Defence, on short vs long weapons), Ringeck/Liechtenauer glosses. ' +
      '(2) documented DEFLECTION technique against a spear/polearm point -- what physically redirects a ' +
      'thrusting point offline (a sword\'s cross/forte, a hand-parry, a body-void), and what the deflecting ' +
      'weapon\'s own morphology needs to do it (the project already has a leverage() primitive: grip_len minus ' +
      'a fraction of head_len -- does this match how treatises actually describe short-vs-long leverage, or is ' +
      'something missing?). (3) documented consequences for the LONGER weapon once distance is closed -- can it ' +
      'still function, does it have to shorten grip (half-staff/half-sword equivalents for polearms), what ' +
      'happens if it cannot retract in time. (4) is there a documented MINIMUM distance a weapon needs to ' +
      'develop a full-power swing or thrust (the "a greatsword cannot be fully swung if the opponent is 50cm ' +
      'away" intuition) -- treatise evidence for shortened/checked strikes in close vs full strikes at range.' },
  { key: 'facing_stance',
    prompt: 'Research historical FACING/STANCE conventions in European and Asian sword/polearm traditions: ' +
      '(1) SQUARE stance (both shoulders facing the opponent, like a modern boxing stance) vs BLADED/OBLIQUE ' +
      'stance (one shoulder forward, presenting a narrower target and greater reach on that side) -- which ' +
      'traditions/weapon-classes favour which, and WHY (what does each afford: lateral mobility vs reach vs ' +
      'target profile vs which grip/technique options are available from it). Cite Fiore\'s poste (guards), ' +
      'Meyer\'s Leger, Italian rapier stance (Capoferro, Fabris -- explicitly oblique/bladed for maximum reach ' +
      'with minimum target), and any evidence on two-handed polearm/greatsword stance (is it more square, given ' +
      'both hands commit to the haft rather than one hand leading a blade?). ' +
      '(2) how facing affects footwork for GAP MANAGEMENT specifically -- is a squared stance associated with ' +
      'more lateral/circling footwork (voiding sideways) while a bladed stance is associated with more linear ' +
      'advance/retreat (passing steps, lunges)? (3) how facing affects which grip changes / which strikes ' +
      '(swing vs thrust) are readily available from a given stance without a full reset.' },
  { key: 'commitment_depth',
    prompt: 'Research THRUST/STRIKE COMMITMENT DEPTH and its force/recovery tradeoff, and RANGE-UTILIZATION ' +
      '(whether a weapon has room to develop its full strike). (1) documented distinction between a quick ' +
      '"feeling" thrust/probe vs a fully committed lunge/thrust in fencing treatises (Capoferro/Fabris\'s ' +
      'passata/scannatura, Fiore\'s posta lunga vs a checked thrust, Destreza\'s measured attacks) -- what makes ' +
      'a deep committed strike deliver more force (full arm/body extension, weight transfer, hip rotation) vs a ' +
      'shallow one, and what it costs (recovery time, exposure). (2) documented recognition that a weapon ' +
      'cannot deliver its normal power if the target is CLOSER than its optimal striking distance -- treatise ' +
      'or biomechanical evidence for "checked" or "half" blows delivered at short range (a cut that cannot ' +
      'complete its arc, a thrust that cannot extend the arm) vs full-distance strikes, and any half-sword/' +
      'half-staff equivalents (gripping higher up a long weapon specifically to regain effective range in close ' +
      '-- the project already models grip-choking via WP.at_grip/grip_target; does treatise evidence suggest ' +
      'this is the RIGHT physical response, or is something else documented, e.g. a shortened swing arc rather ' +
      'than a grip change?). (3) any biomechanical/sports-science grounding for strike-force vs joint-extension ' +
      'percentage (e.g. boxing punch-force studies on distance-to-target vs power, which might transfer).' },
  { key: 'grappling',
    prompt: 'Research historical GRAPPLING actions integrated into armed combat: grabbing the opponent\'s ' +
      'weapon (shaft or blade), grabbing the opponent\'s arm/wrist, and PINNING (trapping a limb or weapon ' +
      'between one\'s own arm and body, underfoot, or against the ground). Cite Fiore\'s Abrazare (unarmed ' +
      'grappling) and his armed plays that transition into grappling (disarms, arm-locks from a bind), ' +
      'Ringen am Schwert (wrestling-at-the-sword in the German tradition, Ott Jud/Ringeck), and any polearm-' +
      'specific grappling (hooking with a guisarme/bec-de-corbin, then pulling into a grapple or pin -- the ' +
      'project already has hook/catch morphology data for several polearms in ' + ENG + '/weapons.py, check ' +
      'those). Specifically document: (1) under what RANGE/CONTACT conditions a grab is attempted (does it ' +
      'require an existing bind, or can it be reached for from open measure?). (2) what makes a grab/pin ' +
      'SUCCEED or FAIL physically (reach to the target part, a free hand, the opponent\'s weapon morphology -- ' +
      'is a haft/shaft easier to grab than a hilt?). (3) documented CONSEQUENCES once a weapon or limb is ' +
      'grabbed/pinned -- what can the grabbed fighter still do, how do they escape, what follow-up does the ' +
      'grabber get (the project has a currently-INERT `clinch` field per weapon, 1-10 scale, meant to capture ' +
      'grappling affinity -- note what it should plausibly represent once wired live).' },
]

phase('Research')
var results = await parallel(CLUSTERS.map(function (c) {
  return function () {
    var p = c.prompt + '\n\n' + DISCIPLINE + '\n\nWrite your JSON to: ' + OUT + '/' + c.key + '.json'
    return agent(p, { label: 'research:' + c.key, phase: 'Research', model: 'sonnet' })
  }
}))
log('Researched ' + results.filter(Boolean).length + '/' + CLUSTERS.length + ' clusters.')

phase('Synthesize')
var files = CLUSTERS.map(function (c) { return OUT + '/' + c.key + '.json' })
var synth = await agent(
  'Synthesize a single combined research brief for the Valoria scene-combat closing-distance/facing/grip ' +
  'subsystem redesign. Read ALL of these JSON files:\n' + files.join('\n') + '\n\n' + DISCIPLINE +
  '\n\nYour job: (1) cross-check for CONTRADICTIONS between clusters (e.g. does the facing_stance research\'s ' +
  'account of oblique-stance reach match the commitment_depth research\'s account of full-extension mechanics?) ' +
  'and flag any; (2) identify which findings are STRONGLY grounded (multiple treatise citations, or explicit ' +
  'biomechanical evidence) vs WEAKLY grounded (a single source, or an inference) -- this matters for how much ' +
  'design latitude the next phase has; (3) produce ONE combined, organized brief a system designer could work ' +
  'from directly, preserving all citations. Do NOT propose formulas, gains, or game-mechanic designs yourself -- ' +
  'that is the next phase\'s job; stay in the facts/grounding lane.\n\n' +
  'Write TWO outputs:\n1. ' + OUT + '/combined_brief.md -- the organized, cited brief.\n' +
  '2. ' + OUT + '/flags.json -- {"contradictions": [...], "weakly_grounded": [...], "strongly_grounded_highlights": [...]}.\n\n' +
  'Your final MESSAGE must be short: confirm both files written + the top 3 flags.',
  { label: 'synthesize', phase: 'Synthesize', model: 'opus' })

return { results: results.length, synth: synth }
