export const meta = {
  name: 'social-contest-design',
  description: 'Prior-art mining (acclaimed social-conflict games) + integration/ripple analysis for the Valoria social contest subsystem, batched in small waves',
  phases: [
    { title: 'PriorArt', detail: '4 research agents survey acclaimed social-conflict designs across media and map concrete lessons to this system' },
    { title: 'Ripple', detail: '5 agents read the coupled subsystems and report coherence, ripple effects, and integration gaps' },
  ],
}

const REPO = 'cwd = C:/Github/ttrpg. Repo is a TTRPG/video-game design corpus (rules text is the source of truth).'

const SYSTEM_SUMMARY = [
  'THE VALORIA SOCIAL CONTEST (the subject system), in brief:',
  '  - A scripted, exchange-based debate/persuasion duel descended from Burning Wheel Duel of Wits.',
  '  - Setup picks an adjudicator type (Expert Judge=Cognition / Crowd=Charisma / No-adjudicator=Attunement / Panel),',
  '    a primary genre (Memory vs Projection), an argument style = genre + orientation (Revealing/Obscuring), and a',
  '    Persuasion Track (0-10; >=7 Side A, <=3 Side B, 4-6 compromise) with audience Resistance from faction Stability.',
  '  - Each exchange: Appraise (read opponent/audience) -> optional Corroborate -> Argue (pool = Primary x2 + History',
  '    + genre/orientation/Recall dice) -> Resolve by interaction type CLASH/REINFORCE/CROSS/TIE -> strain to loser',
  '    (vs Composure = Cha x3) and Concentration depletion (Spent at 0).',
  '  - Outcomes: Decisive win -> binding Obligation (tracked as a clock; constrains NPC priority trees), Domain Echo',
  '    (faction Mandate / +1D Domain Action), Thread co-movement (Mending Stability), Conviction Scars on NPCs, Chain',
  '    Contests on Compromise. Variants: Royal Audience, Church Tribunal, Excommunication, Succession Contest, BG',
  '    Parliamentary Vote, Hybrid.',
  '  - The canonical track name is actually "Piety Track" (derived_stats §14.2/§11); the spec lags using "Persuasion Track".',
].join('\n')

const FINDINGS_DIGEST = [
  'A consistency audit already confirmed 22 defects in this subsystem, including: Concentration formula split',
  '((3xFocus)+(2xSpirit) vs struck Focusx3); Cha-mod/Foc-defence x3 scaling applied inconsistently; Rattled still +Ob',
  'instead of -1D (channel violation); a SUPERSEDED twin file (social_contest_system_v2.md) still cited by ~a dozen docs;',
  'Recall lingering in pools after removal; three different Appraise specs; two unreconciled resistance-erosion rules;',
  'Persuasion-vs-Piety track naming; several dangling cross-references. Treat these as KNOWN; your job is design/integration,',
  'not re-finding them.',
].join('\n')

// ---------- PriorArt schema ----------
const PRIOR_ART_SCHEMA = {
  type: 'object',
  properties: {
    tradition: { type: 'string' },
    exemplars: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          title: { type: 'string' },
          medium: { type: 'string' },
          why_noteworthy: { type: 'string', description: 'acclaim / awards / influence, and why relevant here' },
          mechanic: { type: 'string', description: 'the specific social-conflict / dialogue / persuasion mechanic' },
          lesson_for_valoria: { type: 'string', description: 'a CONCRETE change or validation for the Valoria contest' },
          targets: { type: 'string', description: 'which Valoria mechanic or audit finding it informs' },
        },
        required: ['title', 'medium', 'mechanic', 'lesson_for_valoria'],
      },
    },
    top_recommendations: { type: 'array', items: { type: 'string' }, description: '2-4 highest-value adoptions/changes' },
    does_it_make_sense: { type: 'string', description: 'from this tradition: is an exchange-based social CONTEST the right frame, or would another model fit better?' },
  },
  required: ['tradition', 'exemplars', 'top_recommendations'],
}

// ---------- Ripple schema ----------
const RIPPLE_SCHEMA = {
  type: 'object',
  properties: {
    subsystem: { type: 'string' },
    couplings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          mechanic: { type: 'string' },
          direction: { type: 'string', description: 'contest->subsystem, subsystem->contest, or bidirectional' },
          target: { type: 'string', description: 'the stat/clock/track/arc affected' },
          coherent: { type: 'boolean', description: 'is this coupling well-formed and consistent with the wider engine?' },
          note: { type: 'string', description: 'evidence quote or file/section; flag gaps' },
        },
        required: ['mechanic', 'direction', 'target', 'coherent', 'note'],
      },
    },
    ripple_summary: { type: 'string', description: 'how a contest outcome propagates outward through this subsystem' },
    integration_gaps: { type: 'array', items: { type: 'string' } },
    fit_verdict: { type: 'string', description: 'from this subsystem: does the social contest make sense / earn its complexity here?' },
  },
  required: ['subsystem', 'couplings', 'ripple_summary', 'fit_verdict'],
}

const PRIOR_ART_LANES = [
  {
    key: 'tabletop-rpg',
    prompt: [
      'Survey ACCLAIMED / influential TABLETOP RPG systems for social conflict, debate, and persuasion resolution.',
      'The Valoria contest is explicitly a descendant of Burning Wheel\'s DUEL OF WITS — analyze that lineage first',
      '(statements, Body of Argument, scripted simultaneous exchanges, obligations, "the rules let you lose the argument',
      'and win the point"), then go beyond it: Apocalypse World / PbtA (fictional positioning, manipulate/seduce moves,',
      'the deliberate refusal to inflict social "damage" on PCs), Mouse Guard/Torchbearer conflicts, King Arthur',
      'Pendragon (Passions & Traits forcing rolls), Cortex/Smallville (Values & Relationships as the dice), Reign (one-roll',
      'engine, mass social), Houses of the Blooded, Chuubo\'s, Legacy: Life Among the Ruins (faction play). For each, give',
      'the specific mechanic and a CONCRETE lesson for the Valoria contest.',
    ].join('\n'),
  },
  {
    key: 'narrative-videogames',
    prompt: [
      'Survey ACCLAIMED narrative / RPG VIDEO GAMES whose social, dialogue, or intrigue systems are noteworthy:',
      'Disco Elysium (skills-as-voices, internal checks, white/red checks, Thought Cabinet), Pentiment (no combat;',
      'persuasion via background/knowledge; consequences over seasons), Alpha Protocol (stances: Professional/Suave/',
      'Aggressive, reputation, timed dialogue), Pathologic, Citizen Sleeper, Sunless Sea/Skies, Crusader Kings II/III',
      '(stress, intrigue, hooks/obligations, schemes), Roadwarden, Planescape: Torment. For each acclaimed exemplar give',
      'the specific mechanic and a CONCRETE lesson for the Valoria contest (especially the Appraise/read step, genre/',
      'orientation choice, Obligations, Conviction Scars, and the video-game continuous-engine mode).',
    ].join('\n'),
  },
  {
    key: 'if-vn-courtroom',
    prompt: [
      'Survey ACCLAIMED INTERACTIVE FICTION, VISUAL NOVELS, and courtroom/debate games: Ace Attorney / Phoenix Wright',
      '(cross-examination: press statements, present EVIDENCE to expose contradictions), Danganronpa (class trials,',
      'truth bullets, rebuttal showdowns), Choice of Games / ChoiceScript (stat-gated persuasion, opposed-stat checks,',
      'fairmath), Fallen London / StoryNexus (qualities, challenges, "a chance to..."), 80 Days, Hades (relationship/',
      'keepsake systems), text-parser IF (Galatea for conversation modeling). For each, give the specific mechanic and a',
      'CONCRETE lesson — pay special attention to how "citing named evidence to contradict a claim" (Ace Attorney) maps',
      'to Valoria\'s Recall +2D citation bonus and Evidence-Track findings, and how stat-gated branching maps to the',
      'Persuasion/Piety Track.',
    ].join('\n'),
  },
  {
    key: 'negotiation-political',
    prompt: [
      'Survey ACCLAIMED negotiation / political / systems games (digital and board): Suzerain (governing via dialogue,',
      'promises with political cost), Reigns (binary swipes balancing four faction meters), Diplomacy (negotiation as the',
      'whole game), Twilight Struggle (influence/area control, events), Frostpunk (laws & moral cost), This War of Mine,',
      'Dune: Imperium / area-majority influence games, Republic/Democracy-style policy sims. For each, give the specific',
      'mechanic and a CONCRETE lesson for Valoria\'s faction-scale layer: the BG Parliamentary Vote, Obligations as binding',
      'commitments, Domain Echo, Mandate/Stability meters, and whether the personal<->faction (Hybrid/zoom) coupling has',
      'good precedent.',
    ].join('\n'),
  },
]

const RIPPLE_LANES = [
  {
    key: 'faction-victory',
    prompt: [
      'Trace how the social contest couples into the FACTION / PROVINCIAL / VICTORY layer. Read (Grep/Glob then Read the',
      'relevant sections): designs/provincial/faction_layer_v30.md, designs/provincial/victory_v30.md, designs/provincial/',
      'faction_politics_v30.md, and any clock_registry doc. Trace: Obligations -> clocks -> Mandate/Stability and NPC',
      'priority-tree constraints; Domain Echo -> Domain Actions; BG Parliamentary Vote; Succession Contest -> faction split;',
      'Excommunication -> Mandate/CI. Judge whether each coupling is coherent and whether the contest earns its place at',
      'faction scale.',
    ].join('\n'),
  },
  {
    key: 'thread-cosmology',
    prompt: [
      'Trace how the social contest couples into THREADWORK / COSMOLOGY. Read designs/threadwork/threadwork_v30.md and the',
      'social_contest_v30 sections §9.3 (Practitioner Weaving), §9.4 (Thread Operations Between Exchanges), §9.4b',
      '(Adjudicator Thread Response), §6 (Thread co-movement -> Mending Stability), and Heresy/Excommunication via Crown',
      'Index (CI). Trace how a contest outcome ripples to Mending Stability, CI, and Heresy proceedings, and whether the',
      'Thread-in-contest coupling (visibility gates, temporal-axis conflict, adjudicator certainty response) is coherent.',
    ].join('\n'),
  },
  {
    key: 'npc-conviction',
    prompt: [
      'Trace how the social contest couples into NPC BEHAVIOR and CONVICTION. Read designs/npcs/npc_behavior_v30.md, any',
      'conviction_track / conviction docs, and params/contest_extensions.md (Resonant Style Targeting). Trace: Resonant',
      'Style targeting -> +1D / Scars; Conviction Scars -> NPC arc transitions; Obligations -> NPC priority-tree blocking;',
      'Disposition shifts -> Reputation. Note the audit-flagged deprecated Conviction labels (Continuity/Reason) and the',
      'Piety-Track usage. Judge coherence and whether the contest is the right driver for NPC conviction change.',
    ].join('\n'),
  },
  {
    key: 'scale-agency',
    prompt: [
      'Trace how the social contest couples into SCALE TRANSITIONS and PLAYER AGENCY. Read designs/architecture/',
      'scale_transitions_v30*.md and designs/architecture/player_agency_v30.md. Trace: BG <-> TTRPG <-> Hybrid contest',
      'modes; Mandatory Zoom-In triggers (Heresy interrogation, Stability crisis); Scene Slate / Chain Contests on',
      'Compromise; Standing >= 5 eligibility for Succession. Judge whether mode-switching and zoom coupling are coherent',
      'and whether they create double-resolution or gaps.',
    ].join('\n'),
  },
  {
    key: 'engine-combat-parallel',
    prompt: [
      'Assess whether the social contest is STRUCTURALLY PARALLEL to COMBAT and consistent with the shared ENGINE. Read',
      'designs/scene/combat_v30.md, designs/scene/derived_stats_v30.md §14 (the 4-bucket taxonomy: Pools/Derived/Tracks/',
      'Clocks), and params/core.md (channel reservation Pool vs Ob). Compare: Argue Pool vs Combat Pool; Composure/',
      'Concentration vs Health/Stamina; strain vs damage; Rattled/Spent vs wounds/out-of-breath; the channel-reservation',
      'rule. Judge whether the contest reuses the engine primitives consistently (it is supposed to mirror combat) and',
      'where it diverges in a way that is a defect vs a deliberate asymmetry.',
    ].join('\n'),
  },
]

function priorArtThunk(lane) {
  return () => agent(
    'You are a game-design researcher. ' + REPO + '\n\n' + SYSTEM_SUMMARY + '\n\n' + FINDINGS_DIGEST + '\n\nTRADITION: ' + lane.key + '\n' + lane.prompt + '\n\nUse WebSearch (load it via ToolSearch: query "select:WebSearch") to confirm titles, acclaim, and mechanic details where useful, and keep claims accurate (do not invent games or awards). Be concrete: every exemplar must end in a specific, actionable lesson for the Valoria contest. tradition="' + lane.key + '".',
    { label: 'priorart:' + lane.key, phase: 'PriorArt', schema: PRIOR_ART_SCHEMA },
  ).catch(() => null)
}

function rippleThunk(lane) {
  return () => agent(
    'You are a systems-integration analyst for the Valoria TTRPG. ' + REPO + '\n\n' + SYSTEM_SUMMARY + '\n\n' + FINDINGS_DIGEST + '\n\nSUBSYSTEM: ' + lane.key + '\n' + lane.prompt + '\n\nGround every coupling in a file/section reference or short verbatim quote you actually read. subsystem="' + lane.key + '".',
    { label: 'ripple:' + lane.key, phase: 'Ripple', schema: RIPPLE_SCHEMA },
  ).catch(() => null)
}

async function inWaves(thunks, size) {
  const out = []
  for (let i = 0; i < thunks.length; i += size) {
    const res = await parallel(thunks.slice(i, i + size))
    for (const r of res) { if (r) out.push(r) }
    log('completed ' + Math.min(i + size, thunks.length) + '/' + thunks.length)
  }
  return out
}

phase('PriorArt')
const priorArt = await inWaves(PRIOR_ART_LANES.map(priorArtThunk), 2)

phase('Ripple')
const ripple = await inWaves(RIPPLE_LANES.map(rippleThunk), 2)

log('design pass complete: ' + priorArt.length + ' prior-art lanes, ' + ripple.length + ' ripple lanes')

return { priorArt, ripple }
