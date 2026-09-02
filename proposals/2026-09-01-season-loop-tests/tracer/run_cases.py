"""Route every case's `season_requires` rows onto probes, execute, and grade.

THE HONESTY RULES, inherited from the in-chain instrument (#351) because its own report
records what went wrong without them, and re-tightened here:

  1. **Probe verdicts are HARD; case verdicts are ADVISORY.** A probe is an execution. A case
     verdict is a keyword routing over prose, and keyword routing is crude.
  2. **A row that does not route is reported UNMAPPED, never passed.** Silence is not a pass.
  3. **A case more than half of whose `core` rows fail to route is NOT-ASSESSED**, not graded.
     Grading it PLAYABLE would be the instrument flattering the shape by failing to aim at it.
  4. **Every route matches on WORD BOUNDARIES with explicit negative guards.** #351's most
     expensive correction was a bare substring `ambient` catching ambient-MATERIAL rows (8 -> 3)
     and a bare `counter` matching inside "counter-productive" (10 -> 8). Both are guarded here.
  5. **A probe runs ONCE.** Its verdict is cached, so a case cannot change a probe's result.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import probes as P
from shape import ShapeGap
from trace_log import TRACE

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CHAIN = ROOT.parent / "2026-08-31-shape-tracer" / "cases"


# ---------------------------------------------------------------------------
# THE ROUTER. (probe_id, regex, negative-guard regex or None)
# Word-boundary anchored. Ordered: the FIRST match wins, so specific precedes general.
# ---------------------------------------------------------------------------

ROUTES: list[tuple[str, str, str | None]] = [
    # --- the sharpest structural refusals, matched before anything general ---
    ("A3",  r"\b(end|conclude|close|resolv\w+|trigger\w*|fire\w*)\b[^.]{0,70}\b(threshold|counter|meter|clock|track|gauge|tally)\b(?!\s*-\s*productive)", r"counter-?productive|countermand"),
    ("A3",  r"\b(threshold|counter|meter|gauge)\b(?!\s*-\s*productive)[^.]{0,70}\b(without|with no|no one|nobody|automatic\w*)\b[^.]{0,40}\b(decid\w+|choos\w+|person|actor)", None),
    ("W3",  r"\b(ambient|background|passive|scheduled|automatic)\b[^.]{0,60}\b(mood|morale|unrest|discontent|loyalty|opinion|attitude|sentiment|trust|reputation|standing|legitimacy)\b", None),
    ("W3",  r"\b(mood|morale|unrest|discontent|loyalty|sentiment)\b[^.]{0,60}\b(drift|decay|erode|worsen|sour|degrade|rise|fall)\b[^.]{0,40}\b(on its own|without|no one|nobody|automatic)", None),
    ("A34", r"\b(decay|erode|lapse|fade|atroph\w+|sink)\b[^.]{0,60}\b(neglect|inattention|disuse|not tend\w*|untended|nobody)\b", None),
    # ⚠ The in-chain "ambient MATERIAL vs ambient SOCIAL" correction recurring on a new axis.
    # W4's carrier is a SITE; a row about a PERSON's condition degrading has no carrier in the
    # design at all, which is what P32 raises. Guarded so person-rows fall through to it.
    ("W4",  r"\b(ambient|environmental|material|physical|substrate|land|soil|climate|weather)\b[^.]{0,60}\b(worsen|degrade|decay|deplete|erode|change|shift)\w*\b",
     r"\b(his|her|their|personal|character'?s?|person'?s?|practitioner'?s?)\b[^.]{0,30}\bcondition\b"),

    # --- the person ---
    ("P1",  r"\b((no|without|lacking)\s+(\w+\s+){0,2}(office|post|rank|position|standing|title|command|duty|seat)|unranked|postless|ordinary person|low[- ]agency|holds nothing)\b", None),
    ("P2",  r"\b(several|multiple|more than one|many|five|5)\b[^.]{0,40}\b(action|act|scene|thing)s?\b[^.]{0,40}\b(season|turn)\b", None),
    ("P2",  r"\bchoose what to (leave undone|drop|abandon|forgo|sacrifice)\b|\btriage\b", None),
    ("P3",  r"\b(decide|act|choose|reason)\b[^.]{0,60}\b(from|on)\b[^.]{0,30}\b(what they (believe|know)|their own (belief|knowledge|information)|partial|incomplete|limited) (information|knowledge|view|picture)?\b", None),
    ("P4",  r"\b(false|wrong|mistaken|incorrect|untrue|erroneous)\b[^.]{0,50}\b(belief|conclusion|information|rumou?r|impression|understanding)\b", None),
    # ⚠ `hidden` alone matched hidden QUANTITIES and hidden GROWTH -- P17's and P28's
    # territory -- and handed them P5's PASS, which asserts only that Event has no `actor`.
    # P5 is about ATTRIBUTION, so an attribution term is now required.
    ("P5",  r"\b(covert|secret|clandestine|anonymous|unattributed|deniable|misattribut\w+|wrongly blam\w+|framed?)\b[^.]{0,70}\b(act|action|deed|attribut\w+|blame|credit|author|who did|responsib\w+|identity)\b", None),
    ("P5",  r"\b(who (did|carried out|was behind) it|attribut\w+ to the wrong|blamed for (another|someone else))\b", None),
    ("P6",  r"\b(conviction|moral|value|principle|belief about (right|wrong)|scruple)s?\b[^.]{0,60}\b(chang\w+|shift\w+|move\w+|erode|harden|revis\w+)\b", None),
    ("P7",  r"\b(scar\w*|trauma|lasting (moral|psychological) (damage|harm|cost)|guilt|corrupt\w+ by)\b", None),
    ("P8",  r"\b(thwart\w*|obstruct\w*|frustrat\w*|beat\w* (them )?to|denied by|taken by another|lose out)\b", None),
    ("P8",  r"\bblock\w*\b[^.]{0,60}\b(by another|by someone|a rival|an opponent|another (person|character|actor)|competitor)\b", None),
    ("P9",  r"\b(order|command|instruct|dispatch|direct|assign)\w*\b[^.]{0,60}\b(subordinate|underling|agent|servant|officer|deputy|soldier|follower)\b", None),
    ("P9",  r"\b(refuse|disobey|deviat\w+|ignore|defy)\b[^.]{0,50}\b(order|command|instruction|directive)\b", None),
    ("P10", r"\b(ongoing|multi[- ]?(week|season|month)|repeated|sustained|continuing|in[- ]progress|work[- ]in[- ]progress|over (several|multiple) seasons)\b[^.]{0,60}\b(task|work|labou?r|project|effort|activity)\b", None),
    ("P11", r"\b(skill|competence|rank|ability|capability|training|expertise)\b[^.]{0,60}\b(gate|restrict|prevent|forbid|bar|lock|unavailable|unlock)\w*\b", None),
    ("P12", r"\b(option|choice|available action|thing they (may|can) do|opportunit\w+)s?\b[^.]{0,50}\b(comput\w+|deriv\w+|generat\w+|emerg\w+|not (an )?authored)\b", None),
    ("P13", r"\b(need|hunger|subsistence|survival|want|starv\w+|food|eat)\w*\b[^.]{0,60}\b(driv\w+|motivat\w+|shap\w+|press\w+|force)\b", None),
    # THE GUARD IS THE POINT. "a STANDING armed institution", "a STANDING coercive threat",
    # "a STANDING external-threat orientation" use `standing` as an ADJECTIVE meaning permanent.
    # Unguarded, this route claimed 18 core rows and made `standing` the single largest blocker
    # in both test sets -- the same defect class as the in-chain run's bare `ambient` (8 arcs
    # became 3) and bare `counter` (matching inside "counter-productive", 10 became 8).
    # ⚠ FOURTH RECURRENCE OF THE BARE-TOKEN CLASS. The rev-2 guard was a 15-noun WHITELIST and
    # "a persistent, STANDING CONDITION" walked straight through it. A whitelist is the wrong
    # shape here: the adjectival sense takes an open class of nouns. The guard is now
    # structural -- `standing` followed by ANY noun is adjectival unless the sentence is about
    # a person's regard.
    # ⚠ FOURTH AND FIFTH RECURRENCE, and rev 3's structural guard was wrong in BOTH directions:
    # too narrow (it excluded "his standing must fall"), and still too wide (it needed
    # whitespace + a lowercase letter, so "standing," and "Standing" slipped through). Replaced
    # with a POSITIVE requirement -- `standing` must sit beside a regard verb or a
    # with/among/before complement -- which is what the noun sense actually looks like.
    ("P14", r"\b(esteem|prestige|how .{0,20}(is|are) (seen|regarded|perceived)|public (image|perception))\b", None),
    ("P14", r"\bstanding\b[^.]{0,30}\b(with|among|before|in the eyes of|at court)\b", None),
    ("P14", r"\b(his|her|their|the character'?s?|the person'?s?)\s+standing\b[^.]{0,40}\b(rise|fall|improv\w+|declin\w+|suffer|recover|chang\w+|depend)\w*\b", None),
    ("P15", r"\b(private|secret|confidential|in confidence|unobserved|behind closed doors|no one else (hears|knows|sees))\b[^.]{0,60}\b(conversation|meeting|act|deed|word|exchange)\b", None),
    ("P16", r"\b(differ\w*|disagree\w*|diverge\w*|conflict\w*)\b[^.]{0,60}\b(account|version|belief|understanding|perspective|view|memor\w+)s?\b", None),
    ("P17", r"\b(accumulat\w+|build\w* up|mount\w*|grow\w*|creep\w*|trickle)\b[^.]{0,70}\b(risk|suspicion|exposure|attention|scrutiny|heat|pressure|notice)\b", None),
    ("P18", r"\b(forc\w+|compel\w*|oblig\w+|require\w*|summon\w*)\b[^.]{0,70}\b(choos\w+|decid\w+|answer|respond|act|face)\b", None),
    ("P20", r"\b(individuat\w+|become a named|step out of (the )?(crowd|cohort|mass)|emerge as an individual|named individual)\b", None),
    ("P21", r"\b(crowd|cohort|mass|population|group of people|mob|the many|villagers|townsfolk)\b[^.]{0,60}\b(act|behave|decid\w+|move|respond)\w*\b", None),
    ("P22", r"\b(possess\w+|hold\w*|custody|carry\w*|own\w*)\b[^.]{0,70}\b(object|document|record|text|copy|item|token|writ|letter)\b", None),
    ("P23", r"\b(vanish|disappear|be killed|murder\w*|die|assassinat\w+|simply gone)\b[^.]{0,60}\b(no (institutional|formal|legal) (process|proceeding|trial)|outside every institution|without (a )?trial)\b", None),
    ("P23", r"\b(kill(ed|ing|s)?|murder\w*|assassinat\w+)\b", None),
    ("P24", r"\b(death|dies|dying|killed)\b[^.]{0,70}\b(end|terminat\w+|vacat\w+|release|dissolv\w+)\w*\b[^.]{0,40}\b(post|office|tenure|holding|position|obligation)\b", None),
    ("P26", r"\b(accumulat\w+|repeated|sustained|cumulative|over (several|many) seasons)\b[^.]{0,60}\b(harm|damage|injur\w+|wound|suffering|deprivation|loss)\b", None),
    ("P27", r"\b(underperform\w*|shirk\w*|slack\w*|quietly do(ing)? less|drag\w* (their )?feet|foot[- ]?drag|comply in (letter|form) (but )?not)\b", None),
    ("P28", r"\b(read|see|inspect|access|know)\b[^.]{0,40}\b(another'?s?|other people'?s?|someone else'?s?)\b[^.]{0,30}\b(memor\w+|mind|belief|knowledge|ledger|thought)\w*\b", None),
    ("P29", r"\b(travel|journey|move|relocat\w+|go|march|ride|sail)\w*\b[^.]{0,60}\b(between|from one|to another|across|elsewhere|another (place|region|territory|settlement))\b", None),
    ("P30", r"\b(remember|memor\w+|recall|persist\w*|carry (over|forward)|survive)\w*\b[^.]{0,60}\b(across|between|from one|beyond|next)\b[^.]{0,20}\bseasons?\b", None),

    # --- factions, offices, petitions ---
    ("F1",  r"\b(faction|cause|movement|party|order|society|network|conspirac\w+|alliance)\b[^.]{0,70}\b(span\w*|across|member\w*|join\w*|adher\w*|shar\w*)\b", None),
    ("F2",  r"\b(dissolv\w+|collaps\w+|abandon\w*|memberless|defunct|die out|leave)\b[^.]{0,70}\b(faction|cause|movement|order|party|group)\b", None),
    # ⚠ The institutional noun must be the GRAMMATICAL SUBJECT of the verb. Every row in this
    # corpus is phrased "X must be able to Y", so a wide window made the clause nearly free --
    # and rows about A THIRD PARTY, A PERSON, or an institution HOLDING something were graded
    # L1-FORBIDDEN. `party`, `house`, `power` and `order` are dropped: all four are ordinary
    # words for people and things in this corpus.
    ("F3",  r"\b(the )?(faction|church|crown|state|guild|council|institution|dicastery)\b\s+(itself\s+)?(must be able to\s+)?(act|decide|choose|move|take (an )?action)\w*\b", None),
    # `make` alone let F4 claim rows about an office making an action HARDER -- the exact
    # opposite of what F4's PASS asserts (S11.1: "an office adds NO verb and NO modifier").
    ("F4",  r"\b(office|post|position|title|appointment|seat|rank)\b[^.]{0,70}\b(grant|confer|entitle|permit|authoris|authoriz|eligib)\w*\b", None),
    ("F4",  r"\bmakes? (an? )?(ordinary )?(action|act)\b[^.]{0,40}\b(available|possible|open)\b", None),
    ("F5",  r"\b(no (fixed )?(seat|place|territory|home)|trans[- ]?(settlement|regional)|dispersed members|scattered members)\b", None),
    ("F5",  r"\b(members?|executors?|officers?)\b[^.]{0,50}\b(everywhere|across the realm|in every|scattered)\b", None),
    ("F6",  r"\b(never (heard|received|learned)|fail\w* to (arrive|reach)|undelivered|did not reach|distort\w*|garbl\w+|misunderstood in transit)\b", None),
    ("F7",  r"\b(petition|appeal|demand|request|grievance|complaint|plea|suit)\w*\b[^.]{0,70}\b(before|to|reach\w*|put\b|rais\w*|bring\w*|carr\w+|heard by)\b[^.]{0,60}\b(office|council|court|tribunal|body|assembly|venue|authority|superior|holder|seat|sitting|patron|magistrate|someone who)\b", None),
    ("F7",  r"\b(no power|powerless|without influence|lowly|humble)\b[^.]{0,70}\b(get|bring|put|reach)\b[^.]{0,40}\b(matter|issue|case|concern)\b", None),
    ("F8",  r"\b(sitting|tribunal|council|court|assembly|body|panel|committee|board|hearing)\b[^.]{0,70}\b(decid\w+|rul\w+|determin\w+|judg\w+|adjudicat\w+|vote|find)\b", None),
    ("F9",  r"\b(many|several|multiple|repeated\w*|over and over|spray|whole season)\b[^.]{0,60}\b(petition|appeal|request|approach|meeting)s?\b", None),
    ("F10", r"\b(scarce|scarcity|limited|finite|not enough|shortfall|run out|empt\w+|compet\w+ for the same)\b[^.]{0,70}\b(resource|grain|store|supply|fund|money|capacity|slot|seat)\w*\b", None),
    ("F11", r"\b(true|actual|real|genuine)\b[^.]{0,40}\b(strength|size|membership|extent|reach|power)\b[^.]{0,40}\b(faction|movement|cause|network|order)\b", None),
    ("F12", r"\b(appoint\w*|confer\w*|invest(ed|iture|s)?|promot\w*|revok\w*|depos\w*|dismiss\w*|remov\w*|strip\w*|elevat\w*)\b[^.]{0,60}\b(office|post|position|rank|title|seat|command)\b", r"\binvestigat\w+"),
    ("F13", r"\b(vacan\w+|empty (seat|post|office)|succession|fall\w* (empty|vacant)|replace\w* .{0,20}(who died|the dead))\b", None),
    ("F14", r"\b(count|tally|total|measure|track)\w*\b[^.]{0,60}\b(territor\w+|holding|ground|land|province|region)s?\b[^.]{0,40}\b(gain|lose|control|hold)\w*\b", None),
    ("F15", r"\b(staff|establishment|clerk|retainer|servant|household|subordinate|deput\w+|secretar\w+)s?\b[^.]{0,70}\b(work|perform|execut\w+|carr\w+ out|do the)\b", None),

    # --- the world ---
    ("W1",  r"\b(disrepair|decay|dilapidat\w+|ruin|silt|crumbl\w+|deteriorat\w+|fall\w* apart|wear)\b[^.]{0,70}\b(place|site|harbour|harbor|mine|road|building|structure|land|infrastructure)\b", None),
    ("W1",  r"\b(no longer|can(not|'t) be done|unavailable|closed off|lost)\b[^.]{0,60}\b(there|at (that|the) (place|site|location))\b", None),
    ("W2",  r"\b(world|things|events)\b[^.]{0,60}\b(chang\w+|move\w*|continu\w+|happen\w*|churn\w*|proceed\w*)\b[^.]{0,60}\b(no (player|character|one)|without (a|the) player|unattended|absent|nobody (is )?(there|present|watching))\b", None),
    ("W5",  r"\b(harvest|yield|crop|granary|foodstuff)\b[^.]{0,70}\b(good|bad|vary|var\w+|better|worse|fail|abundant|come in|season)\w*\b", None),
    ("W6",  r"\b(plague|famine|storm|flood|disaster|epidemic|blight|catastrophe|calamity)\b", None),
    ("W7",  r"\b(expire|lapse|ttl|time limit|valid until|run\w* out of time|deadline pass\w*)\b", None),
    ("W8",  r"\b(case|charge|accusation|investigation|inquiry|proceeding|prosecution|trial)\b[^.]{0,70}\b(ripen\w*|advance\w*|proceed\w*|progress\w*|mature\w*|build\w*)\b", None),
    # ⚠ FIFTH RECURRENCE OF THE BARE-TOKEN CLASS, and the costliest yet. The trailing `\w*`
    # applies to the WHOLE alternation, so `age` matched AGENT, AGENTS, AGENCY and AGENDA --
    # and the arc corpus's only PLAYABLE verdict was rows about "two AGENTS belonging to rival
    # external powers" collecting W9's births-and-deaths PASS. The stems are now closed.
    ("W9",  r"\b(births?|born|death rates?|populations?|demograph\w+|generations?|age|aged|ageing|aging)\b", None),
    ("W10", r"\b(unrest|discontent|legitimacy|reputation|morale|cohesion|stability|order)\b[^.]{0,60}\b(level|value|amount|score|rating|degree|stat)\b", None),
    ("W11", r"\b(eat|feed|subsist|draw|consume|provision)\w*\b[^.]{0,60}\b(from|out of|on)\b[^.]{0,40}\b(store|larder|granar\w+|supply|stock|hearth|household)\w*\b", None),
    ("W12", r"\b(populate\w*|world[- ]?gen\w*|seed\w* the world|people who (hold|have) no|ordinary inhabitant|the rest of the population)\b", None),

    # --- the architecture ---
    # ⚠ A1 PROVOKES `causes=[]` to demonstrate the refusal; routing provenance rows to it
    # graded them BLOCKED, reporting the design's causes[] rule as the thing that BLOCKS
    # causal reconstruction. A2 is the probe that DEMONSTRATES provenance, and it passes.
    ("A2",  r"\b(what caused|caus\w+ chain|provenance|traceab\w+|why (it|this) happened|reconstruct\w* .{0,20}(story|history))\b", None),
    ("A2",  r"\b(sequence|chain|thread|series|string) of (related |connected |linked )?(event|happening|incident|episode|moment)s?\b", None),
    ("A2",  r"\b(read back|replay|review|recount|narrat\w+)\b[^.]{0,50}\b(as (one|a single) story|the whole story|what happened)\b", None),
    ("A4",  r"\b(same|identical|reproducib\w+|determinis\w+|repeatab\w+)\b[^.]{0,60}\b(seed|start\w*|initial condition|input|run)\w*\b", None),
    ("A5",  r"\b(order|sequence)\b[^.]{0,50}\b(must not|should not|independent|does not (matter|depend))\b", None),
    ("A6",  r"\b(church|crown|state|the order|the guild|the council|the court|the tribunal|the dicastery)\b\s+(excommunicat|declar|proclaim|issu|rul|decre|condemn|sanction)\w*\b", None),
    ("A7",  r"\b(battle|duel|fight|siege|combat|hearing|trial|debate|examination|argument|contest|confrontation)\b[^.]{0,70}\b(resolv\w+|decid\w+|play\w* out|run|conduct\w*)\b", None),
    ("A8",  r"\b(within|inside|during)\b[^.]{0,40}\b(a|the|another)\b[^.]{0,20}\b(contest|battle|hearing|conflict|fight)\b", None),
    ("A9",  r"\b(see|read|know|inspect|observe|access)\b[^.]{0,50}\b(what is happening|the state|conditions|affairs)\b[^.]{0,50}\b(elsewhere|another (region|place|province|settlement)|other (regions|places))\b", None),
    ("A10", r"\b(sum\w*|total|aggregate|across all|throughout|over (all|every)|combined|overall)\b[^.]{0,60}\b(within|inside|under|contained|beneath|subordinate)\b", None),
    ("A14", r"\b(react|respond|counter|retaliat|answer)\w*\b[^.]{0,60}\b(within|in|during|inside)\b[^.]{0,30}\bthe same (season|turn)\b", None),
    ("A15", r"\b(spiral|feedback|self[- ]?(feeding|reinforcing|sustaining)|runaway|escalat\w+ without|vicious cycle|never end\w*)\b", None),
    ("A16", r"\b(region|area|place|province|part of the (world|map))\b[^.]{0,60}\b(own (pace|clock|schedule|rate)|advance independently|different speed)\b", None),
    ("A18", r"\b(module|subsystem|component|piece of the (game|engine))\b[^.]{0,60}\b(declar\w+|interface|contract|boundar\w+|I/O|inputs? and outputs?)\b", None),
    ("A19", r"\b(swap\w*|replac\w*|plug\w*|attach\w*|register\w*)\b[^.]{0,60}\b(module|subsystem|component|provider|implementation)\b", None),
    ("A21", r"\b(broadcast|announce\w*|publish\w*|proclaim\w*|promulgat\w*|issu\w*)\b[^.]{0,70}\b(all|every|everyone|throughout|realm[- ]wide|widely)\b", None),
    ("A22", r"\b(each|every|per)\b[^.]{0,30}\b(region|settlement|province|container|area)\b[^.]{0,60}\b(run|process|resolv|advance|handle)\w*\b[^.]{0,40}\b(own|separately|independently|its)\b", None),
    ("A24", r"\b(same|one|single|uniform|identical)\b[^.]{0,40}\b(mechanism|rule|system|machinery|treatment)\b[^.]{0,60}\b(scale|level|size|elite|population|both)\w*\b", None),
    ("A25", r"\b(span\w*|cross\w*|reach\w*|extend\w*|stretch\w*)\b[^.]{0,50}\b(several|multiple|many|more than one)\b[^.]{0,30}\b(region|duch\w+|province|territor\w+|settlement)\w*\b", None),
    ("A27", r"\b(who (writes|owns|changes|updates)|ownership|owned by|responsib\w+ for (writing|changing))\b", None),
    ("A28", r"\b(record|log|history|chronicle)\b[^.]{0,60}\b(consistent|intact|integrity|complete|not (be )?corrupt)\w*\b", None),
    ("A29", r"\b(separate|own|its own|distinct)\b[^.]{0,30}\b(record|log|history|register)\b[^.]{0,40}\b(subsystem|combat|battle|contest)\b", None),
    ("A31", r"\b(how many|number of|count of|exactly)\b[^.]{0,40}\b(action|act|scene|moment|thing)s?\b[^.]{0,40}\b(season|turn)\b", None),
    ("A32", r"\b(scene|playable moment|act)s?\b[^.]{0,60}\b(per season|budget|count|number of|how many|allowance|equals?|equival\w+)\b", None),
    ("A33", r"\b(distort\w*|garbl\w*|chang\w* in (transit|the telling)|whisper|rumou?r spread|version that reaches)\b", None),
    ("A35", r"\b(godot|engine version|4\.\d)\b", None),
]

COMPILED = [(pid, re.compile(rx, re.I), re.compile(neg, re.I) if neg else None)
            for pid, rx, neg in ROUTES]


def route(need: str) -> str | None:
    for pid, rx, neg in COMPILED:
        if rx.search(need):
            if neg is not None and neg.search(need):
                continue
            return pid
    return None


# ---------------------------------------------------------------------------
# EXECUTION -- a probe runs ONCE; its verdict is cached.
# ---------------------------------------------------------------------------

_VERDICTS: dict[str, dict] = {}


def run_probe(pid: str) -> dict:
    if pid in _VERDICTS:
        return _VERDICTS[pid]
    spec = P.PROBES[pid]
    TRACE.case = f"probe:{pid}"
    try:
        msg = spec["fn"]()
        if isinstance(msg, str) and msg.strip() == "UNREACHABLE":
            # The probe expected the shape to REFUSE and it did not. That is never a PASS:
            # it is either a real finding (a refusal ARCHITECTURE.md states is not enforced)
            # or an instrument defect. Both flatter the shape, so both are reported.
            v = dict(id=pid, verdict="NOT-REFUSED", detail=(
                "the shape PERMITTED what this probe expected it to refuse; the refusal named at "
                f"{spec['section']} did not fire"), kind="NOT-REFUSED",
                section=spec["section"], title=spec["title"])
        else:
            v = dict(id=pid, verdict="PASS", detail=msg, kind=None,
                     section=spec["section"], title=spec["title"])
    except ShapeGap as g:
        v = dict(id=pid, verdict="GAP", detail=g.what, kind=g.kind,
                 section=g.where, title=spec["title"], needs=g.needs, law=g.law)
    except AssertionError as e:
        v = dict(id=pid, verdict="INSTRUMENT-ERROR", detail=f"assertion failed: {e!r}",
                 kind=None, section=spec["section"], title=spec["title"])
    except Exception as e:                                  # noqa: BLE001
        v = dict(id=pid, verdict="INSTRUMENT-ERROR", detail=f"{type(e).__name__}: {e}",
                 kind=None, section=spec["section"], title=spec["title"])
    v["by"] = spec["by"]
    v["tests"] = spec["tests"]
    _VERDICTS[pid] = v
    return v


# ---------------------------------------------------------------------------
# CASES
# ---------------------------------------------------------------------------

def _tolerant_yaml(text: str, fname: str):
    """The in-chain #351 corpus is COMMITTED WITH AN AGENT-TRANSCRIPT PREAMBLE AND MARKDOWN
    FENCES: six of its seven case files do not load with `yaml.safe_load`, and one
    (`ARC3.yaml`) is TRUNCATED AT ITS HEAD -- its first record's `- id:` line was lost when
    committed, leaving an ORPHANED FRAGMENT of a third emergent case above `EMG-10`.

    Both are real defects in the chain's own evidence base. They are RECORDED (CORPUS_DEFECTS)
    and worked around at LOAD time, never fixed in place: the committed files are the chain's
    evidence and this instrument does not edit evidence.

    The orphan's rows are NOT DROPPED. Dropping them would silently delete real `season_requires`
    needs; they are recovered under a synthetic id that says what happened."""
    import yaml
    fenced = re.search(r"```(?:yaml)?\n(.*?)```", text, re.S)
    body = fenced.group(1) if fenced else text
    notes: list[str] = []
    if fenced:
        notes.append(f"{fname}: committed inside a markdown fence with transcript preamble")
    try:
        return yaml.safe_load(body) or [], notes
    except yaml.YAMLError:
        pass
    lines = body.splitlines()
    first = next((i for i, ln in enumerate(lines) if ln.startswith("- id:")), None)
    if first is None:
        notes.append(f"{fname}: UNPARSEABLE and holds no `- id:` record")
        return [], notes
    cases = yaml.safe_load("\n".join(lines[first:])) or []
    head = "\n".join(lines[:first]).strip()
    if head:
        notes.append(
            f"{fname}: TRUNCATED AT HEAD -- {first} lines of a record above the first `- id:`; "
            "its identity is unrecoverable from the file")
        # ⚠ REV 5. The reconstruction below FAILED SILENTLY for four revisions -- the fragment
        # begins mid block-scalar, `yaml` raised, the except branch returned [], and TWO `core`
        # ROWS WERE LOST while this function's docstring said "NOT DROPPED" and the regression
        # test asserted only that a NOTE existed. The recovery now starts at the fragment's
        # first parseable `- need:` and REPORTS how many rows it could not reach.
        rows, lost = [], 0
        head_lines = lines[:first]
        start = next((i for i, ln in enumerate(head_lines)
                      if ln.lstrip().startswith("- need:")), None)
        if start is None:
            lost = len(head_lines)
        else:
            lost = start
            try:
                indent = len(head_lines[start]) - len(head_lines[start].lstrip())
                body = "\n".join(ln[indent:] if len(ln) > indent else ln
                                  for ln in head_lines[start:])
                rows = yaml.safe_load(body) or []
                rows = [r for r in rows if isinstance(r, dict) and "need" in r]
            except yaml.YAMLError:
                rows, lost = [], len(head_lines)
        notes.append(f"{fname}: recovered {len(rows)} row(s) from the truncated head; "
                     f"{lost} line(s) above the first parseable `- need:` are UNRECOVERABLE")
        if rows:
            cases = [dict(id=f"{fname.split('.')[0]}-ORPHAN",
                          name="[IDENTITY LOST] headless fragment recovered from a truncated file",
                          one_line="A third emergent case whose `- id:` header was lost when the corpus was committed.",
                          scale="world", season_requires=rows,
                          ends_when="unrecoverable -- the record's tail is present, its head is not")] + cases
    return cases, notes


CORPUS_DEFECTS: list[str] = []


def load_cases(kind: str) -> list[dict]:
    """`kind` in {NPC, ARC}. NPC cases come from BOTH the in-chain #351 corpus (27) and this
    session's completion of it (19) -- together the full 46 in the registry. ARC cases are
    the in-chain corpus in full."""
    out: list[dict] = []
    seen: set[str] = set()
    sources = []
    if kind == "NPC":
        sources = sorted(CHAIN.glob("NPC*.yaml")) + sorted((ROOT / "cases").glob("NPC*.yaml"))
    else:
        sources = sorted(CHAIN.glob("ARC*.yaml")) + sorted((ROOT / "cases").glob("ARC*.yaml"))
    for f in sources:
        data, notes = _tolerant_yaml(f.read_text(), f.name)
        CORPUS_DEFECTS.extend(notes)
        for c in data or []:
            if c.get("id") in seen:
                continue
            seen.add(c["id"])
            c["_source"] = f.name
            out.append(c)
    return out


def grade(case: dict) -> dict:
    rows = case.get("season_requires") or []
    routed, unmapped, unclear = [], [], []
    for r in rows:
        need = r.get("need", "")
        entry = dict(need=need, hardness=r.get("hardness", "important"), probe=None)
        # An `UNCLEAR:` row is the CASE SOURCE failing to say something, not the shape failing
        # to do it. Counting it as UNMAPPED conflates two different failures, and the in-chain
        # brief is explicit that an unclear source IS ITSELF DATA.
        if re.match(r"\s*UNCLEAR\b", need, re.I):
            unclear.append(entry)
            continue
        pid = route(need)
        entry["probe"] = pid
        if pid is None:
            unmapped.append(entry)
        else:
            entry["verdict"] = run_probe(pid)
            routed.append(entry)

    core = [r for r in rows if r.get("hardness") == "core"
            and not re.match(r"\s*UNCLEAR\b", r.get("need", ""), re.I)]
    core_unmapped = [u for u in unmapped if u["hardness"] == "core"]
    core_routed = [r for r in routed if r["hardness"] == "core"]
    core_blocked = [r for r in core_routed
                    if r["verdict"]["verdict"] in ("GAP", "NOT-REFUSED")]

    # HONESTY RULE 3, TIGHTENED. A case more than half of whose core rows failed to route is
    # NOT-ASSESSED -- the instrument did not aim at it.
    #
    # AND THE STRICTER CLAUSE, ADDED AFTER READING THE FIRST PLAYABLE LIST: **a case with ANY
    # unmapped `core` row may not be graded PLAYABLE.** Five of the twelve PLAYABLE verdicts in
    # the first run rested on one or two routed core rows with other core rows sitting
    # unmapped beside them -- one case reached PLAYABLE on a single distinct probe with three
    # rows unrouted. That is the instrument certifying a season it never aimed at, which is the
    # flattering direction and the one nobody notices.
    #
    # A blocker still outranks it: if a core row DID route and DID hit a gap, the case is
    # BLOCKED regardless of what else failed to route, because that is a fact about the shape
    # rather than about the aim.
    if core_blocked:
        verdict = "BLOCKED"
    elif core and len(core_unmapped) * 2 > len(core):
        verdict = "NOT-ASSESSED"
    elif not core_routed:
        verdict = "NOT-ASSESSED"
    elif core_unmapped:
        verdict = "NOT-ASSESSED"
    elif any(r["verdict"]["verdict"] in ("GAP", "NOT-REFUSED") for r in routed):
        verdict = "DEGRADED"
    else:
        verdict = "PLAYABLE"

    return dict(
        id=case["id"], name=case.get("name", ""), scale=case.get("scale", ""),
        source=case.get("_source", ""), verdict=verdict,
        rows=len(rows), core=len(core), core_routed=len(core_routed),
        core_unmapped=len(core_unmapped), core_blocked=len(core_blocked),
        blockers=sorted({r["probe"] for r in core_blocked}),
        routed=routed, unmapped=unmapped, unclear=len(unclear),
        ends_when=case.get("ends_when", ""),
    )


def main(kinds=("NPC", "ARC")) -> dict:
    report: dict = {}
    for kind in kinds:
        cases = load_cases(kind)
        graded = []
        for c in cases:
            TRACE.case = c["id"]
            graded.append(grade(c))
        report[kind] = graded
    # every probe runs, even if no case routed onto it -- an unexercised probe is a finding.
    for pid in P.PROBES:
        run_probe(pid)
    report["_probes"] = _VERDICTS
    report["_gaps"] = TRACE.gaps
    report["_trace_counts"] = TRACE.counts()
    report["_corpus_defects"] = sorted(set(CORPUS_DEFECTS))
    return report


# ---------------------------------------------------------------------------
# SECOND-TIER ROUTES. Added after MEASURING which `core` rows failed to route on tier one.
# Routing improves the instrument's AIM. It cannot change a probe's verdict, which executes
# once and is cached -- so widening the router cannot flatter the shape, only aim at it.
# Tier one is consulted first, so a specific route still beats a general one.
# ---------------------------------------------------------------------------

ROUTES_2: list[tuple[str, str, str | None]] = [
    ("P31", r"\b(unstated|unspoken|private|personal|unrecognis\w+|unrecogniz\w+|unconscious\w*|hidden|concealed)\b[^.]{0,60}\b(motive|interest|agenda|reason|incentive|stake|loyalt\w+)\b", None),
    ("P31", r"\b(bias|skew|colou?r|tilt|slant|shape)\w*\b[^.]{0,70}\b(decision|judgement|judgment|choice|assessment|evaluation)s?\b", None),
    ("P32", r"\b(degrad\w+|deteriorat\w+|exhaust\w+|deplet\w+|worsen\w*|narrow\w*|wear\w* down)\b[^.]{0,70}\b(condition|capacity|health|available action|range of action|option)s?\b", None),
    ("P32", r"\b(fixed|predictable|named|specific)\b[^.]{0,30}\border\b[^.]{0,70}\b(narrow|withdraw|crisis|down to|full freedom)\b", None),
    ("P33", r"\b(cost|price|expense|toll|pay)\w*\b[^.]{0,70}\b(scal\w+|proportion\w*|var\w+|more|greater|higher|type and scale)\b", None),
    ("P33", r"\b(persistent personal resource|personal resource|reserve|stamina|strain budget)\b", None),
    ("P34", r"\b(only|sole|single|no other)\b[^.]{0,30}\b(living )?(actor|person|holder|one|individual)\b[^.]{0,60}\b(know|hold|remember|possess|retain)\w*\b", None),
    ("P34", r"\b(institutional memory|founding agreement|original terms|exact knowledge of|what was actually agreed)\b", None),
    ("P35", r"\b(reputation|standing|regard|credit|esteem)\b[^.]{0,70}\b(separate|distinct|different|second|another)\b[^.]{0,30}\b(track|register|ledger|channel|audience|from any)\b", None),
    ("P35", r"\b(never (be )?(publicly|openly) (credit|acknowledg|recognis|recogniz|nam))\w*\b", None),
    ("P36", r"\b(branch|fork|split|diverge)\w*\b[^.]{0,50}\b(two|three|four|several|multiple)\b[^.]{0,20}\bways?\b", None),
    ("P36", r"\b(protect|report|leverage|expose|shield)\b[^.]{0,40}\b(him|her|them|the discovery|the finding)\b", None),
    ("F16", r"\b(faction|institution\w*|organis\w+|organiz\w+|order|guild|church|crown)\b[^.]{0,60}\b(stat|resource|pool|treasury|coffers|capital|points?|\bAP\b|score|track)\b", None),
    ("F16", r"\b(grow|raise|increase|spend|deplete|drain|expend|improve)\w*\b[^.]{0,60}\b(faction[- ]wide|institutional|shared|pooled)\b[^.]{0,40}\b(resource|stores?|treasury|supplies|material|capacity)\b", None),
    ("F16b", r"\b(grow|raise|increase|erode|drain)\w*\b[^.]{0,60}\b(faction[- ]wide|institutional|shared|pooled)\b[^.]{0,40}\b(loyalty|unrest|legitimacy|morale|standing|cohesion)\b", None),
    ("F17", r"\b(approval|authoris\w+|authoriz\w+|sponsorship|sanction|permission|sign[- ]?off|warrant|conduit)\b[^.]{0,70}\b(precondition|prerequisite|required|necessary|formal|before (they|he|she|it) (can|may))\b", None),
    ("F18", r"\b(conflict|cut against|compet\w+|at odds|tension|contradict|in direct)\w*\b[^.]{0,70}\b(order|instruction|directive|mandate|command|what .{0,25}(ordered|wanted|demanded))\b", None),
    ("F19", r"\b(settlement|place|town|region|province|community|territor\w+|world)\b[^.]{0,60}\b(generat\w+|produc\w+|rais\w+|surfac\w+|throw\w* up|of its own)\b[^.]{0,50}\b(demand|need|dispute|shortfall|ambition|problem|issue|pressure)s?\b", None),
    ("A36", r"\b(first|earlier|prior|before)\b[^.]{0,60}\b(foreclos\w+|close off|rule out|prevent|preclud\w+|constrain)\w*\b[^.]{0,50}\b(later|after|subsequent|remaining)\b", None),
    # ⚠ `order` is a common noun in this corpus meaning A COMMAND or AN INSTITUTION; this route
    # is about ACT-ORDERING. Requires the sequencing sense explicitly.
    ("A36", r"\b(sequenc\w+|the order (in )?which|ordering|resolution order)\b[^.]{0,50}\b(within|inside|during)\b[^.]{0,30}\b(a|the|one|the same)\b[^.]{0,15}\bseason\b", None),
    ("P22", r"\b(evidence|proof|dossier|report|record|document|data|finding|text|copy|letter|writ|file|artefact|artifact)\b[^.]{0,70}\b(persist\w*|exist\w*|outliv\w*|survive|be (found|seized|carried|hidden|given|destroyed|examined|stolen|traded))\w*\b", None),
    ("P5",  r"\b(true|false|fabricat\w+|forg\w+|falsif\w+|invent\w+|planted|misleading)\b[^.]{0,70}\b(unable to distinguish|cannot tell|indistinguishable|without knowing|in advance|which is which)\b", None),
    ("P16", r"\b(corroborat\w+|refut\w+|verif\w+|confirm\w+|cross[- ]check)\w*\b[^.]{0,70}\b(independent\w*|third part\w+|another|separately|own (fieldwork|investigation))\b", None),
    ("P17", r"\b(silent\w*|quiet\w*|undetect\w+|undiscovered|unnoticed|invisibl\w+)\b[^.]{0,70}\b(accumulat\w+|build|grow|mount|increas\w+|compound)\w*\b", None),
    ("P18", r"\b(ultimatum|reckoning|moment of truth|come to a head|forced (moment|choice|decision))\b", None),
    ("P18", r"\bcrisis\b[^.]{0,70}\b(forc\w+|compel\w*|demand\w*|requir\w+|must (then )?(choose|decide|answer|act))\b", None),
    ("P26", r"\b(burden|toll|strain|attrition|erosion|grind|damage)\b[^.]{0,70}\b(accumulat\w+|reach\w*|mount\w*|personal\w*|build|cumulative)\w*\b", None),
    ("P2",  r"\b(limited|finite|renewing|per[- ]season|fixed)\b[^.]{0,40}\b(budget|allowance|capacity|menu|number of (action|act))\w*\b", None),
    ("P9",  r"\b(compl(y|ies|ied)|complian\w+|negotiat\w+|defy|defian\w+|obey|disobey)\w*\b[^.]{0,60}\b(order|mandate|directive|instruction|demand|command)s?\b", None),
    ("F12", r"\b(recall|reassign|transfer|dismiss|retire|succeed|replace|elevat\w+|instal)\w*\b[^.]{0,50}\b(from|to|in|into)\b[^.]{0,25}\b(post|office|position|command|seat|role)\b", None),
    ("F7",  r"\b(bring|take|carr\w+|escalat\w+|refer|put)\w*\b[^.]{0,50}\b(to|before|up to|in front of)\b[^.]{0,45}\b(council|tribunal|court|authority|superior|body|office|assembly|patron)\b", None),
    ("F8",  r"\b(ruling|verdict|decision|determination|judgement|judgment|finding)\b[^.]{0,60}\b(binding|formal|issued|handed down|reached|made by)\b", None),
    ("A2",  r"\b(arc|storyline|campaign|plot|narrative|situation)\b[^.]{0,60}\b(unfold|develop|progress|advance|play out|emerge|resolve)\w*\b", None),
    ("A15", r"\b(cascad\w+|snowball|amplif\w+|reinforc\w+|feed\w* (back|on itself)|spiral|vicious circle|runaway)\b", None),
    ("A15", r"\bcompound\w*\b[^.]{0,70}\b(without (bound|limit|end)|indefinitely|each season|no (stopping|terminal|end)|unchecked)\b", None),
    ("A18", r"\b(unrelated|separate|independent|different|other)\b[^.]{0,40}\b(system|subsystem|mechanic|module|part of the (game|engine))s?\b[^.]{0,60}\b(interact|connect|link|affect|reach|couple)\w*\b", None),
    ("W8",  r"\b(deadline|term|clock|timer|countdown|schedule|due date)\b[^.]{0,60}\b(set|declar\w+|wound|start\w*|run\w*|expir\w*|matur\w*)\b", None),
    ("P30", r"\b(state|status|condition|progress|change|memory)\b[^.]{0,50}\b(track\w*|persist\w*|carried|retained|stored|remembered)\b[^.]{0,45}\b(season|turn|time)s?\b", None),
    ("P1",  r"\b(ordinary|common|humble|lowly|unremarkable|private|non[- ]?institutional|non[- ]faction)\b[^.]{0,30}\b(person|individual|character|inhabitant|subject|actor)\b", None),
    ("P21", r"\b(cohort|as a group|many people at once|collectively|acts? as one)\b", None),
    ("P21", r"\bweight\b[^.]{0,40}\b(cohort|population|crowd|group|many|number of people)\b", None),
    ("F4",  r"\b(remit|jurisdiction|mandate|writ|competence|authority|purview)\b[^.]{0,60}\b(cover|extend|reach|limit|bound|defin|includ)\w*\b", None),
    ("F15", r"\b(staff|establishment|clerk|retainer|servant|household|deput\w+|secretar\w+|subordinate)s?\b[^.]{0,70}\b(work|perform|execut\w+|carr\w+ out|do the|actually)\b", None),
    ("A27", r"\b(who|which)\b[^.]{0,20}\b(writes|owns|changes|updates|is responsible for)\b", None),
    ("A31", r"\b(exactly|precisely|how many|number of)\b[^.]{0,40}\b(action|act|scene|moment|attempt)s?\b", None),
]

COMPILED += [(pid, re.compile(rx, re.I), re.compile(neg, re.I) if neg else None)
             for pid, rx, neg in ROUTES_2]


ROUTES_3: list[tuple[str, str, str | None]] = [
    # ⚠ W8 MUST PRECEDE W13. S13.1 supplies the mechanism for "a case ripens while the accused
    # does nothing" and calls it the better design: the act DECLARES the stages and their terms,
    # MATTER matures them, and each maturation is a person's past act ripening. Rev 3 routed
    # that sentence to W13's fourth-clock refusal, so ARC-04 was BLOCKED on a row THE HEAD
    # EXPLICITLY ANSWERS -- the instrument measuring against the design.
    ("W8",  r"\b(procedural|formal|legal|accusatory|disciplinary|case|charge|tribunal)\b[^.]{0,45}\b(stage|step|phase|process|proceeding|timetable)s?\b[^.]{0,70}\b(advance|proceed|progress|matur\w+|ripen\w*|on its own|regardless)\w*\b", None),
    ("F3",  r"\b(faction|institution|guild|church|polity|dicastery)\b\s+(itself\s+)?must be able to\s+(choose|decide|fund|ally|spend|act|pursue|adopt|escalat\w+|behav\w+|respond)\w*\b", None),
    ("F3",  r"\b(each|every|a) faction'?s?\b[^.]{0,50}\b(autonomous|default|own)\b[^.]{0,40}\b(action|behaviou?r|strategy|tendency|posture)\b", None),
    ("W13", r"\b(fixed|regular|annual|seasonal|periodic|automatic)\b[^.]{0,30}\b(schedule|tick|interval|timetable|cadence)\b", None),
    ("W13", r"\b(background|world[- ]scale|global|ambient)\b[^.]{0,40}\b(stat|track|quantity|counter|meter|level)\b[^.]{0,60}\b(decay|declin\w+|drift|erod\w+|fall|deteriorat\w+)\w*\b", None),
    ("P37", r"\b(fixed|automatic|deterministic)\b[^.]{0,25}\b(lookup|table|rule|formula)\b[^.]{0,60}\b(rather than|instead of|not)\b[^.]{0,40}\b(deliberat\w+|choice|decision|judgement|judgment)\b", None),
    ("P37", r"\b(fully|entirely|wholly) determined by\b[^.]{0,60}\b(internal state|own state|stat|disposition|score)\b", None),
    ("P38", r"\b(GM|game ?master|referee|adjudicator|arbiter)\b", None),
    ("P38", r"\b(optimal|ideal|correct|right)\b[^.]{0,25}\b(timing )?window\b[^.]{0,60}\b(clos\w+|without .{0,25}signal|no .{0,20}signal)\b", None),

    ("P26", r"\b(persistent|lasting|lingering|not automatically cleared|carried forward|unresolved)\b[^.]{0,50}\b(condition|state|status|effect|damage|penalt\w+|wound)\b", None),
    ("P17", r"\b(accumulat\w+|aggregate|add up|combine)\w*\b[^.]{0,60}\b(named|single|one|a) (condition|state|threshold|total|summary|effect)\b", None),
    ("A34", r"\b(inaction|doing nothing|non[- ]commitment|neglect|absence of|failure to act|not acting|unattended)\b[^.]{0,70}\b(erod\w+|decay|cost|damag\w+|fall|worsen|los\w+)\b", None),
    ("A2",  r"\b(attribut\w+|trace|credit|blame|identif\w+)\b[^.]{0,60}\b(back to|to which|the cause|who caused|which actor|responsible)\b", None),
    ("F12", r"\b(separate|distinct|further|additional|second)\b[^.]{0,35}\b(mechanical )?(action|step|act)\b[^.]{0,60}\b(implement|enact|enforc\w+|carr\w+ out|actually)\b", None),
    ("P16", r"\b(invisible|imperceptible|undetectable|unknown)\b[^.]{0,35}\bto (him|her|them|himself|herself|themselves|the subject)\b[^.]{0,60}\b(perceptib\w+|visible|detectab\w+|apparent)\b", None),
    ("P22", r"\b(each|both|mutual\w*|simultaneous\w*)\b[^.]{0,40}\b(hold|possess|have)\w*\b[^.]{0,40}\b(evidence|leverage|proof|material|information)\b", None),
    ("P36", r"\b(genuine|real|meaningful)\b[^.]{0,25}\b(two|three|four)[- ]way choice\b", None),
    ("P36", r"\bchoice between\b[^.]{0,90}\bor\b", None),
    ("P18", r"\b(recurring|each season|every season|per[- ]season|repeated)\b[^.]{0,40}\b(risk|chance|check|test|exposure)\b", None),
]

COMPILED += [(pid, re.compile(rx, re.I), re.compile(neg, re.I) if neg else None)
             for pid, rx, neg in ROUTES_3]


ROUTES_4: list[tuple[str, str, str | None]] = [
    # THE TRACKED-QUANTITY FAMILY -- the single largest cluster of unrouted `core` rows in the
    # arc corpus, and the exact family L3 and L5 legislate. THE ORDER IS THE CRUX. The in-chain
    # 50-arc run established the distinction they turn on: 19 of 50 arcs want a crossing to
    # COMPEL A NAMED PERSON TO ACT (lawful under L5) and only 8 want a crossing to PRODUCE AN
    # OUTCOME with nobody deciding (forbidden). Route the compelling sense FIRST, or the
    # instrument reports the corpus as far more hostile to the design than it is -- a
    # measurement error in the shape's DISfavour, which is no more acceptable than one in its
    # favour (S0.1 point 4: asymmetric skepticism is a bias, not a defence).

    # (a) A CROSSING THAT COMPELS A NAMED PERSON -- lawful. L5 exactly.
    ("P18", r"\b(quantity|value|track|counter|meter|level|pressure|score|gauge)\b[^.]{0,80}\b(cross\w*|reach\w*|hit\w*|drop\w*|fall\w*|pass\w*)\b[^.]{0,60}\b(forc\w+|compel\w*|oblig\w+|requir\w+|summon\w*|demand\w*)\b[^.]{0,60}\b(person|actor|ruler|officer|leader|holder|character|someone|them|him|her)\b", None),
    ("P18", r"\b(cross\w*|reach\w*|hit\w*)\b[^.]{0,40}\b(a |the )?(threshold|floor|ceiling|limit|edge)\b[^.]{0,70}\b(forc\w+|compel\w*|demand\w*|requir\w+)\b[^.]{0,50}\b(choice|decision|response|answer|act)\b", None),

    # (b) A CROSSING THAT PRODUCES AN OUTCOME WITH NOBODY DECIDING -- forbidden. L5's refusal.
    ("A3",  r"\b(quantity|value|track|counter|meter|level|health|allegiance|pressure|score)\b[^.]{0,80}\b(reach\w*|hit\w*|drop\w*|fall\w*|bottom\w*)\b[^.]{0,40}\b(its |a |the )?(floor|zero|minimum|bottom|threshold)\b[^.]{0,70}\b(trigger|caus\w+|produc\w+|impos\w+|result|fractur\w+|collaps\w+)\w*\b", None),
    ("A3",  r"\b(automatic\w*|irreversible|structural)\b[^.]{0,40}\b(state change|consequence|outcome|effect|penalty|fracture|collapse)\b[^.]{0,70}\b(trigger\w*|when|on|upon)\b[^.]{0,40}\b(threshold|floor|value|quantity|counter)\b", None),

    # (c) A QUANTITY HELD BY A PLACE -- S10.1: a Rung owns NO social aggregate.
    ("W10", r"\b(per[- ](location|place|region|settlement|territory)|local|regional|site[- ]level)\b[^.]{0,60}\b(quantity|value|track|counter|level|score|awareness|allegiance)\b", None),
    ("W10", r"\b(institution|settlement|region|place|territory|province|force|army)'?s?\b[^.]{0,50}\b(overall |collective |aggregate )?(health|morale|cohesion|effectiveness|stability|readiness)\b", None),

    # (d) A FACTION-SCALE POOLED QUANTITY -- L3, and S14.2 leaves nowhere to put it.
    ("F16", r"\b(faction|institution|organisation|organization|order|church|guild)[- ](scale|wide|level)\b[^.]{0,50}\b(resource|pool|stores?|treasury|capacity|material)\b", None),
    ("F16b", r"\b(faction|institution|organisation|organization|order|church|guild)[- ](scale|wide|level)\b[^.]{0,50}\b(stat|score|track|quantity|value)\b", None),
    ("F16", r"\b(one|a single|shared|common)\b[^.]{0,30}\bfaction[- ]wide\b[^.]{0,30}\bvalue\b", None),

    # (e) A QUANTITY THAT MOVES ON ITS OWN -- a fourth clock. S25.1's three are exhaustive.
    ("W13", r"\b(decay\w*|tick\w*|declin\w+|dwindl\w+|drift\w*|erod\w*)\b[^.]{0,50}\b(every|each|per)\b[^.]{0,25}\b(period|season|turn|year|cycle)\b", None),
    ("W13", r"\b(background|ambient|world)[- ]?(pressure|quantity|track|level|stat)\b[^.]{0,70}\b(ris\w+|mount\w*|grow\w*|advanc\w+|accumulat\w+|mov\w+)\b", None),

    # (f) A PERSONAL TALLY -- L3 clause 2 and clause 3.
    ("P17", r"\b(personal|individual|per[- ]person|own)\b[^.]{0,40}\b(threshold|tally|count|track|quantity|meter|exposure)\b", None),
    ("P17", r"\b(silently|invisibly|quietly|unnoticed)\b[^.]{0,60}\b(register|record|accumulat|count|affect)\w*\b", None),

    # (g) LONG-RUNNING PREPARATION TRACKS -- act-declared terms (S13.1), not a MATTER clock.
    ("W8",  r"\b(long[- ]running|multi[- ]season|ongoing|parallel|independent)\b[^.]{0,40}\b(preparation|progress|project|track|thread|effort)s?\b", None),

    # (h) SCALE COUPLING -- a personal act registering at faction scale.
    ("A25", r"\b(personal|small|individual|local)\b[^.]{0,30}\bscale\b[^.]{0,70}\b(faction|regional|realm|world)[- ]?(scale|level|wide)\b", None),

    # (i) SIMULTANEITY AND INDEPENDENCE ACROSS ACTORS.
    ("F18", r"\b(two|three|several|multiple)\b[^.]{0,40}\b(independent|unrelated|separate)\b[^.]{0,40}\b(actor|faction|institution|part(y|ies))\w*\b[^.]{0,60}\b(simultaneous\w*|at (the )?same time|each|both)\b", None),
    ("A36", r"\b(same|one|single)\b[^.]{0,20}\b(location|place|window|period|season)\b[^.]{0,60}\b(contest\w*|oppos\w+|net effect|in (the )?same (order|sequence))\b", None),
]

COMPILED += [(pid, re.compile(rx, re.I), re.compile(neg, re.I) if neg else None)
             for pid, rx, neg in ROUTES_4]


ROUTES_5: list[tuple[str, str, str | None]] = [
    # Reached by `route_precision.unreachable()`: probes the corpus DOES ask for and that no
    # route pointed at. S44.4 names this exact symptom in the in-chain router -- "ELEVEN
    # UNREACHABLE PROBES and a 46% miss rate" -- so it is measured here rather than assumed.
    ("P42", r"\b(wounded|injured|sick|exhausted|distant|far from|travelling|imprisoned|besieged)\b[^.]{0,70}\b(fewer|less|reduced|limited|constrain\w+)\b[^.]{0,40}\b(action|act|option|capacity)s?\b", None),
    ("A26", r"\b(circular|cycle|cyclic|loop|mutual\w*|refer\w* (back|to each other))\b[^.]{0,60}\b(reference|dependenc\w+|relationship|structure|chain)s?\b", None),
    ("A17", r"\b(one|single|the same)\b[^.]{0,30}\b(resolver|resolution (path|point)|place where outcomes)\b", None),
    ("A13", r"\b(recomput\w+|cache|cached|reus\w+|expensive)\b[^.]{0,60}\b(deriv\w+|calculat\w+|aggregate|value)\b", None),
    ("A23", r"\b(ever|all[- ]time|cumulative|historical|lifetime)\b[^.]{0,40}\b(total|count|tally|number of)\b", None),
    # L3's two clauses are DIFFERENT RULES and the corpus asks for both. Clause 1 (one person's
    # own counter) is PERMITTED by the head and routes to P17; clause 2 (a sum across holders)
    # is refused and routes to P43. Revisions 1-3 sent both to the clause-2 refusal.
    ("P43", r"\b(across|among|throughout|over)\b[^.]{0,40}\b(all|every|the) (member|holder|person|character|inhabitant|follower)s?\b[^.]{0,60}\b(total|sum|aggregate|combined|average|tally)\w*\b", None),
    ("P43", r"\b(cohort|faction|population|group)[- ]wide\b[^.]{0,50}\b(tally|total|sum|average|level)\b", None),
    ("P39", r"\b(two|both)\b[^.]{0,45}\b(named |specific )?(person|official|character|actor|leader)s?\b[^.]{0,60}\b(interact|deal|negotiat|correspond|relate|meet)\w*\b[^.]{0,40}\b(repeated\w*|ongoing|over time|directly|each other)\b", None),
    ("P39", r"\b(relationship|rapport|bond|feud|rivalry|friendship|trust)\b[^.]{0,60}\b(between|with)\b[^.]{0,50}\b(change|evolv|develop|persist|carry|deepen|sour)\w*\b", None),
    ("P40", r"\b(conflict\w*|tension|incompatib\w+|competing|divided|torn)\b[^.]{0,70}\b(obligation|dut(y|ies)|loyalt\w+|allegiance|commitment)s?\b", None),
    ("P40", r"\b(obligation|dut(y|ies)|reporting|confidentialit\w+)\b[^.]{0,60}\b(to|toward)\b[^.]{0,40}\b(two|both|a second|another)\b", None),
    ("P41", r"\b(precedent|prior ruling|established practice|past (ruling|decision)|case law)\b", None),
    ("P41", r"\b(argument|case|plea|advocacy|debate)\b[^.]{0,60}\b(strengthen\w*|weaken\w*|bolster\w*|undermin\w*|stronger|weaker)\b", None),
    ("F20", r"\b(treaty|accord|pact|agreement|compact|concordat|charter)\b[^.]{0,70}\b(constrain|bind|govern|limit|oblig|terms)\w*\b", None),
    ("F21", r"\b(individual|personal|own)\b[^.]{0,35}\b(position|vote|stance|dissent|opinion)\b[^.]{0,70}\b(within|inside|on|registered|recorded|distinct)\b[^.]{0,45}\b(body|council|committee|chapter|assembly|board)\b", None),
    ("F21", r"\b(collective|corporate|body'?s?)\b[^.]{0,35}\b(decision|output|ruling|position)\b[^.]{0,60}\b(individual|member|each)\b", None),
    # remaining recurring shapes with an existing probe
    # ⚠ struck. This route was written to match ONE case row's own phrasing ("more than an
    # identity record"), which is fitting the router to the answer -- S44.4's ruling is
    # "don't route -- declare". It produced NPC-036's PLAYABLE on a single row.
    ("F13", r"\b(successor|succession|who follows|next holder)\b[^.]{0,60}\b(undetermined|contested|uncertain|open|several claimants)\b", None),
    ("F6",  r"\b(in (the leader'?s?|his|her|their) name)\b[^.]{0,70}\b(diverg\w+|differ|depart|deviat\w+|not what)\b", None),
    ("P6",  r"\b(faith|belief|doubt|conviction|principle)\b[^.]{0,60}\b(challeng\w+|shaken|tested|question\w+|privately)\b", None),
    ("P17", r"\b(lock\w* in|permanent\w*|irreversib\w+|unrecover\w+|cannot be undone)\b", None),
    ("P10", r"\b(multi[- ]season|long[- ]term|sustained|positioning)\b[^.]{0,40}\b(campaign|effort|project|build[- ]?up)\b", None),
    ("P1",  r"\b(recognis\w+|recogniz\w+|regarded|treated|acknowledged) as\b[^.]{0,45}\b(leader|head|figure|authority)\b[^.]{0,60}\b(before|without|no)\b[^.]{0,35}\b(formal|official|institutional)\b", None),
]

COMPILED += [(pid, re.compile(rx, re.I), re.compile(neg, re.I) if neg else None)
             for pid, rx, neg in ROUTES_5]


if __name__ == "__main__":
    # W15 -- ONE WRITER PER ARTIFACT. This entrypoint used to write `results.json` and
    # `TRACE.txt` itself, and `report.py` wrote them too from its own `main()` call. Two
    # writers over one artifact set meant whichever ran last won, and the committed markdown
    # went stale by one fix: FOUR ARC CASES WERE WRONG IN A MERGED PR because the caselogs
    # came from one run and `results.json` from another. `report.py` is now the SOLE emitter.
    # This entrypoint still RUNS the corpus -- it is the fastest way to see the tallies -- and
    # it writes nothing. The refusal is enforced by execution, not by this comment:
    # `test_w15_the_run_cases_entrypoint_writes_nothing` runs this file as a script and hashes
    # `runs/` before and after.
    rep = main()
    for kind in ("NPC", "ARC"):
        rows = rep[kind]
        tally: dict[str, int] = {}
        for r in rows:
            tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
        print(f"\n=== TEST {kind}: {len(rows)} cases ===")
        print("   " + " · ".join(f"{v} {k}" for k, v in sorted(tally.items())))
        blockers: dict[str, int] = {}
        for r in rows:
            for b in r["blockers"]:
                blockers[b] = blockers.get(b, 0) + 1
        print("   top core blockers: " + " · ".join(
            f"{k}({v})" for k, v in sorted(blockers.items(), key=lambda kv: -kv[1])[:10]))
        rr = sum(r["rows"] for r in rows)
        um = sum(len(r["unmapped"]) for r in rows)
        print(f"   {rr} season_requires rows, {rr-um} routed, {um} UNMAPPED")
    pv = rep["_probes"]
    tal: dict[str, int] = {}
    for v in pv.values():
        key = v["verdict"] if v["verdict"] != "GAP" else f"GAP:{v['kind']}"
        tal[key] = tal.get(key, 0) + 1
    print(f"\n=== PROBES: {len(pv)} ===")
    print("   " + " · ".join(f"{v} {k}" for k, v in sorted(tal.items())))
    print(f"\n=== TRACE: {TRACE.counts()}")
    print("\nWrote nothing under proposals/2026-09-01-season-loop-tests/. `report.py` is the\n"
          "sole emitter of runs/ (W15, guardrail G7). To regenerate the artifacts:\n"
          "    python report.py")
