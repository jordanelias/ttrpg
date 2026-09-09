# The System, Diagrammed

Seven views of one structure. Each is a different cut, not a different system.

**Nothing here is provisional any more.** The elastic/plastic model of Coherence was ruled
2026-09-07 and the constitutive cost model on 2026-09-08; both views are drawn as settled. Where a
node or edge is the framework's own inference rather than a ruling, the note under that view says so
— see `RULINGS.md` for which is which.

---

## 1. The stack — what configures, what takes-as

The single most important distinction in the framework, and the one most easily got wrong:
**spooling configures; rendering *is* the taking-as.** Not an activity undertaken, and not something
that performs a taking-as — it is one. It is a process nonetheless.

```mermaid
flowchart TD
    ES["<b>Ein Sof</b><br/>infinite positive being<br/>no agency, no direction, no response"]
    LIM{{"<b>the limit</b><br/>epistemically inaccessible<br/>the contraction is originary and uncaused"}}
    SP["<b>spooling</b> — layer 1<br/><i>configures</i><br/>supplies substrate · gives temporal accumulation<br/>the <i>how</i> of constitution"]
    CFG["<b>a configuration</b><br/>threads, with three moments:<br/>actuality · temporality · intelligibility"]
    REND["<b>rendering</b><br/>always-already interpretation of things <i>as</i> something<br/><i>takes-as — does not configure</i>"]
    DET["being taken-as <b>is</b> a determination<br/>on the intelligibility axis"]
    CO["<b>co-movement</b><br/>a determination on one moment<br/>is a determination on all three"]

    ES -.->|"inferred from the rendered side only"| LIM
    LIM --> SP
    SP -->|configures| CFG
    CFG --> REND
    REND --> DET
    DET --> CO
    CO -->|"so rendering moves threads<br/>without doing any work"| CFG
```

**Read the loop.** A configuration is rendered; being rendered is a determination; determinations
co-move; so the configuration is thereby determined across all three moments. No agency anywhere.

---

## 2. Layer profiles — what distinguishes kinds of being

Not kinds of thing. **Which layers are operative.**

```mermaid
flowchart LR
    subgraph L["the three layers"]
        direction TB
        L1["<b>1 · spooling</b><br/>passive, from the ground<br/><i>configures</i>"]
        L2["<b>2 · self-rendering</b><br/>continuous, unconscious<br/>takes-oneself-as human<br/><i>gives the configuring its human shape</i>"]
        L3["<b>3 · deliberate threadwork</b><br/>conscious, trained<br/><i>requires the Leap</i>"]
    end

    H["<b>human</b><br/>1 + 2"]
    D["<b>drifted, shallow reach</b><br/>1 only<br/>reshaped by what meets it"]
    DD["<b>drifted, deep reach</b><br/>1 + 3<br/>self-maintained"]
    T["<b>threadcut</b><br/>3 only<br/>radically singular and alien"]
    LZ["<b>in a Locked Zone</b><br/>2, with nothing arriving<br/>becoming precluded"]

    L --> H
    L --> D
    L --> DD
    L --> T
    L --> LZ
```

**The asymmetry that matters.** For a spooled being, *having* a configuration is given — layer 2 only
shapes it. For a threadcut being nothing configures: **being configured is itself the work**, done
deliberately, moment to moment, or not at all.

---

## 3. An operation, end to end

**Direction decides everything.** The same imbrication carries the cost and the benefit; what the
practitioner is joined to is either being held against the draw or handed back to it.

```mermaid
flowchart TD
    A["practitioner, at rest<br/>layer 2 holding them as human"]
    B["<b>the Leap</b><br/>suspend taking-oneself-as-human<br/>layer 1 continues · outward facing persists residually<br/><i>no intrinsic cost — D-5</i>"]
    C["threads taken <i>as threads</i><br/>because one is no longer<br/>taking them as world"]
    D["<b>imbrication</b><br/>practitioner and target joined<br/>during the working"]
    E{"direction of the working<br/>relative to the futural-potential-legible"}
    F["<b>restorative</b><br/>toward the equilibrium<br/>configurations already tend to"]
    G["<b>manipulative</b><br/>off the attractor<br/>held only by the practitioner"]
    H["<b>destructive</b><br/>a harmony unmade"]
    I["<i>giving to the draw</i><br/>nothing needs holding<br/><b>and the practitioner is drawn too</b>"]
    J["<i>holding against the draw</i><br/>working the target out of equilibrium<br/>is working one's own threads<br/>out of equilibrium"]
    M{"what was the working <b>aimed</b> at?"}
    N["aimed at another<br/>→ moves your present displacement<br/>you recover faster for having done it"]
    O["aimed at your own configuration<br/>→ moves your <b>resting point</b><br/><i>extremely difficult, and possible</i>"]
    K["<b>knots</b> — permanent<br/>residue of the imbrication<br/>carry <i>later</i> events, not the immediate cost"]
    L["re-engagement<br/>layer 2 re-takes-oneself-as-human"]

    A --> B --> C --> D --> E
    E --> F --> I
    E --> G --> J
    E --> H --> J
    I --> M
    M --> N
    M --> O
    N --> L
    O --> L
    J -->|"displacement ÷ your own magnitude"| L
    D --> K

    style O stroke-width:3px
```

**Two things the shape carries that a list of rules would lose.**

- **F and G are the same machinery.** Nothing in the diagram distinguishes them except where the
  working points. Cost is not a penalty attached to certain operations; it is what being imbricated
  with a held shape *consists in*, and the benefit is what being imbricated with a released one
  consists in.
- **The edge into L is divided, not doubled.** A manipulative working's displacement is a fixed
  quantity, and what it is a fraction of is the practitioner (§6.8). A larger vessel is not tougher;
  the same load is simply less of it.

------

## 4. What strains, and why scale is not the variable

```mermaid
flowchart LR
    EQ(["<b>futural-potential-legible</b><br/>the equilibrium in which configurations<br/>stand in harmony, needing no sustaining<br/><br/><i>futural</i> — ahead, not a return<br/><i>potential</i> — not yet actual<br/><i>legible</i> — renderable"])

    R["restorative work<br/>moves toward it"]
    M["manipulative work<br/>holds against it"]

    NS["<b>no strain, at any scale</b><br/>nothing is being held<br/>so scale has nothing to multiply"]
    S["<b>strain</b> ∝ magnitude × duration<br/>the summed difference between<br/>what is held and where things tend"]

    EIN["<b>the Einhir</b><br/>a precarious balance<br/>held for generations at civilizational scale"]
    CAL["<b>the Calamity</b><br/>the balance broke <i>as a balance</i><br/>so every configuration in it broke —<br/>none stood at its own equilibrium"]

    R --> NS
    M --> S
    EQ -.-> R
    EQ -.-> M
    S --> EIN --> CAL

    style EQ fill:none,stroke-width:2px
```

**The knife-edge.** Safety belongs to *restoring equilibrium*, not to the word "Mending" or to good
intentions. Restoring a **remembered** state, or an **intended** one, is a shape the practitioner
chose — and holding configurations there at scale is the Calamity's mechanism exactly.

---

## 5. Coherence — RULED 2026-09-07 / 2026-09-08

> Coherence is a **distance** from the equilibrium proper to being human, not a store that depletes.
> **What it is for:** to make repeated threadwork expensive enough that a practitioner recuperates
> before working again — so it must bite *and* be answerable. A cost with no remedy is a countdown,
> not a discouragement. Two elements below are derived rather than ruled and are marked.

```mermaid
flowchart TD
    BAND["<b>the human band</b><br/>the equilibrium proper to being human<br/>has extent, not a single point"]
    Z["<b>resting point</b><br/>where the configuration settles<br/>once fully recovered<br/><i>the floor — rises easily, falls only under work</i>"]
    STR["<b>stress</b><br/>an operation off the attractor,<br/>or a confrontation that overwhelms<br/><i>always an event</i>"]
    EL["<b>elastic displacement</b><br/>where the being presently is<br/>= resting point + current load<br/>this is what the bands read"]
    PL["<b>plastic set</b><br/>the resting point moves outward<br/>no amount of rest undoes it"]
    SELF["<b>restorative threadwork</b><br/>aimed at one's own configuration<br/><i>extremely difficult, and possible</i>"]
    OTH["<b>became other</b><br/>the resting point has left the band"]

    SENS["<b>thread sensitivity</b><br/>accrues from exposure alone<br/>independent of any threshold"]
    ENV["<b>environment at equilibrium</b><br/>the condition on recovery"]
    MEND["<b>mending</b> — one's own or another's<br/>quickens, never required"]

    BAND --- Z
    Z --> EL
    STR --> EL
    EL -->|"below threshold"| REC(["return over time"])
    REC --> Z
    ENV -.->|"gates"| REC
    MEND -.->|"quickens"| REC
    STR -->|"beyond threshold"| PL
    PL -->|"outward"| Z
    SELF -->|"inward"| Z
    Z -->|"once outside the band"| OTH
    OTH -.->|"the same act is now <b>manipulation</b>:<br/>human is no longer where<br/>this configuration tends"| SELF

    EXP["<b>exposure</b><br/>presence to the substrate's workings"] --> SENS
    SENS -.->|"converts more of the next<br/>encounter into stress"| STR
    SENS -.->|"and divides the cost of<br/>work you choose to do — §6.8"| EL

    style OTH stroke-width:3px
    style BAND stroke-dasharray: 5 5
    style SELF stroke-width:3px
```

**Read the two edges into the resting point together — that pair is the whole model.** Stress pushes
it outward and nothing but deliberate restorative threadwork pulls it back. Rest answers displacement;
only work answers the floor. That is what makes the cost bite without making it a countdown.

**The dotted edge out of *became other* is where irreversibility now lives, and it is derived.** With
the floor movable, the threshold cannot be "the floor stops moving". It is §6.6's ruled knife-edge:
Mending restores the harmony a configuration tends toward, **not a remembered state**. Past the band,
human is no longer where this configuration tends — so the identical-looking act of working it back is
manipulation, held against the draw, performed on a whole person. Nothing about the difficulty changes
at the crossing. What changes is which operation it is.

**The dashed node is the other derived element.** *Being human is a band* is not a ruling; it is what
the rulings force, since with a point the first permanent set would already be the crossing.

**Four things the diagram deliberately does not contain**, each ruled out rather than merely absent:

| absent | why |
|---|---|
| **creep** — sustained low load deforming you | Only events deform. A load below threshold leaves nothing behind, however long held. |
| **fatigue** — cycling below yield accumulating | Same ruling. Ten years beside a Gap sum to nothing. |
| **work hardening** — elastic range changing with use | Range is a constant of the being. Only the resting point moves. |
| **sensitivity as a form of plastic set** | Independent. Exposure teaches; stress deforms. |

**Three readings the shape yields.** A **veteran** rests further out with the same elastic range, so an
identical load carries them deeper — nearer the edge without being more fragile. Someone who **lives
beside a Gap** takes no permanent set from living there, does not recover there, and grows more
sensitive for having been there. And a **practitioner who has drifted and wants back** cannot rest
their way there: they need the hardest operation in the discipline, performed on themselves, or
someone able to aim it at them.

---

## 6. Emergence — what comes through a tear

```mermaid
flowchart TD
    TEAR["a tear in the boundary"]
    SUR["<b>surfeit</b><br/>uncontracted being<br/>floods the opening"]
    W{"how it is rendered<br/>by whoever is present"}
    M1["<b>mode 1</b> · ordinary incursion<br/>rendered as nothing coherent<br/>no layers · deteriorates"]
    M2["<b>mode 2</b> · Providence<br/>rendered briefly or by few<br/>transient · an event, not an entity"]
    M3["<b>mode 3</b> · threadcut<br/>rendered widely and durably as a being<br/>layer 3 only"]
    OP["<b>organisation is radically opaque</b><br/>governed by whatever governs how<br/>organisms unfold in the thread paradigm.<br/>Witnesses render the <i>form as perceived</i>,<br/>within their bounds — they do not<br/>constitute the organisation."]

    TEAR --> SUR --> W
    W --> M1
    W --> M2
    W --> M3
    M3 -.-> OP

    style OP fill:none,stroke-dasharray: 3 3
```

---

## 7. Damage — three distinct things

```mermaid
flowchart LR
    G["<b>Gap</b><br/>an absence where the fabric<br/>requires something<br/><br/>· a standing breach in the boundary<br/>· or where a configuration was removed<br/><br/><i>Gap margins</i> are its edges"]
    LZ["<b>Locked Zone</b><br/>becoming has been precluded<br/>threads no longer move<br/>toward an equilibrium<br/><br/>persists indefinitely — the process<br/>that would undo it is the one precluded"]
    OC["<b>orphaned configuration</b><br/>a present state whose causal<br/>history was removed<br/><br/>decays: depth is accumulated,<br/>and the accumulation is gone"]
    MEND["<b>Mending</b><br/>restarts the becoming<br/>does not put anything back"]

    G -->|"large enough, produces one around itself"| LZ
    LZ --> MEND
    MEND -->|"then the tendency does the rest"| LZ

    style MEND stroke-width:2px
```

**A Gap is not a Locked Zone.** A Gap is an absence; a Locked Zone is a region where nothing tends
anywhere. Whether a Gap *itself* can be Mended is open — Mending restarts becoming, and an absence
has nothing there to restart.

---

## 8. Everything at once

```mermaid
flowchart TB
    subgraph GROUND["ground"]
        ES["Ein Sof · no agency"]
    end
    subgraph CONST["constitution"]
        SP["spooling — configures"]
        REND["rendering — takes-as"]
        EQ["futural-potential-legible"]
    end
    subgraph BEING["beings"]
        HU["human · 1+2"]
        TC["threadcut · 3 only"]
        DR["drifted · 1, or 1+3"]
    end
    subgraph ACT["acting"]
        LEAP["the Leap"]
        OPS["operations<br/>restorative / manipulative / destructive"]
        KN["knots · imbrication"]
    end
    subgraph HARM["damage"]
        GAP["Gap"]
        LOCK["Locked Zone"]
        STRAIN["reality-strain"]
    end
    subgraph EPI["what can be known"]
        ABS["abstraction without capture<br/>2D represents 3D without being 3D"]
        TS["thread sensitivity<br/>sets the resolution"]
        BAR["the barrier<br/>propositions available, inert"]
    end

    ES --> SP --> HU
    SP --> DR
    REND --> HU
    EQ -.-> OPS
    HU --> LEAP --> OPS --> KN
    OPS --> STRAIN
    OPS -->|"manipulative work only,<br/>÷ the practitioner's magnitude"| DR
    STRAIN --> GAP --> LOCK
    TC --> STRAIN
    ABS --> TS --> BAR
    TS -.->|"gates what is captured,<br/>and so what reconfigures you"| DR
```

---

## What the diagrams cannot show

**Amorality.** Being moral requires being human, so drift departs the register in which moral
predicates apply rather than failing within it. There is no axis for this because it is the *absence*
of an axis.

**Singularity.** Threadcut beings are drawn as a box, which is already a lie — they are not a category
with members, and nothing about one licenses an inference about another.

**Two deliberate refusals.** What is owed *to* a being outside the moral register, and whether Solmund
understood what was being made of him. Both are open by ruling, not by omission.
