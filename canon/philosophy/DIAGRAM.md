# The System, Diagrammed

Seven views of one structure. Each is a different cut, not a different system.

**Provisional material is marked.** Two areas are under active discussion and are drawn dashed:
the elastic/plastic model of Coherence, and the constitutive account of operational cost. Everything
else is ruled — see `RULINGS.md`.

---

## 1. The stack — what configures, what takes-as

The single most important distinction in the framework, and the one most easily got wrong:
**spooling configures; rendering takes-as.** Rendering is not an activity performed on anything.

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

```mermaid
flowchart TD
    A["practitioner, at rest<br/>layer 2 holding them as human"]
    B["<b>the Leap</b><br/>suspend taking-oneself-as-human<br/>layer 1 continues · outward facing persists residually"]
    C["threads presentable <i>as threads</i><br/>because presentation-as-world has lapsed"]
    D["<b>imbrication</b><br/>practitioner and target joined<br/>during the working"]
    E{"direction of the working<br/>relative to the futural-potential-legible"}
    F["<b>restorative</b><br/>toward the equilibrium<br/>configurations already tend to"]
    G["<b>manipulative</b><br/>off the attractor<br/>held only by the practitioner"]
    H["<b>destructive</b><br/>a harmony unmade"]
    I["no residual load<br/>nothing needs holding"]
    J["<i>working the target out of equilibrium<br/>is working one's own threads<br/>out of equilibrium</i>"]
    K["<b>knots</b> — permanent<br/>residue of the imbrication<br/>carry <i>later</i> events, not the immediate cost"]
    L["re-engagement<br/>layer 2 re-takes-oneself-as-human"]

    A --> B --> C --> D --> E
    E --> F --> I
    E --> G --> J
    E --> H --> J
    I --> L
    J -.->|"PROVISIONAL — see §5"| L
    D --> K

    style J stroke-dasharray: 5 5
```

> ⚠ **The J path is under discussion.** The cost is constitutive rather than fed back through the
> knot: you suspended your self-rendering to join the target, so taking it out of equilibrium takes
> *you* out. Three questions are open — whether restorative work actively *helps* the practitioner,
> whether displacement scales with the target's, and whether the suspension itself displaces you
> before any operation.

---

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

## 5. Coherence — PROVISIONAL

> ⚠ **This section is under discussion and is not ruled.** What is settled: Coherence is a *distance*
> from the equilibrium proper to being human, not a store that depletes; degradation reaches the
> spooling's configuring; everyone has it; the endpoint is irreversibility, not exhaustion. What is
> being worked out is the elastic/plastic model below.

```mermaid
flowchart TD
    E0["configuration at the human equilibrium"]
    STR["stress<br/>an operation off the attractor,<br/>or confrontation"]
    EL["<b>elastic</b><br/>displaced, recoverable<br/>heals back toward equilibrium over time"]
    FAT["<b>fatigue</b><br/>repeated cycling below yield<br/>still accumulates"]
    PL["<b>plastic</b><br/>permanent set<br/>does not heal"]
    WH["<b>work hardening?</b><br/>permanent set toward substrate access<br/>= thread sensitivity<br/>and less elastic range remaining"]
    CR["<b>creep?</b><br/>sustained low load<br/>Gap margins, residue fields<br/>= Warden environmental erosion"]
    OTH["<b>became other</b><br/>the human equilibrium is no longer<br/>where this configuration tends"]

    E0 --> STR --> EL
    EL -->|"time, rest, being taken-as-human by others?"| E0
    EL --> FAT --> PL
    STR -->|"single sufficient stress"| PL
    CR -.-> PL
    PL --> WH
    PL --> OTH

    style EL stroke-dasharray: 5 5
    style FAT stroke-dasharray: 5 5
    style WH stroke-dasharray: 5 5
    style CR stroke-dasharray: 5 5
```

**Open:** what recovery requires; whether sensitivity gain is *identical* to plastic set or a
component of it distinguished by direction; whether work hardening spends future elastic range;
whether creep is distinct from fatigue.

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
    OPS -.->|"PROVISIONAL"| DR
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
