# SIM-MB-06 Tick-by-Tick Record

**Seed:** 1000000  **Max turns:** 15  **TICKS_PER_PHASE:** 6

## Initial state

- A: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
  - subunit: shape=Line, tier=3, start=(15, 9), advance_dir=-1, unit_type=melee
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
  - subunit: shape=Line, tier=3, start=(5, 9), advance_dir=1, unit_type=melee

### Initial grid
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 6  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 7  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 8  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 9  .  .  .  .  B  B  B  B  B  .  .  .  . 
r10  .  .  .  .  .  .  .  .  .  .  .  .  . 
r11  .  .  .  .  .  .  .  .  .  .  .  .  . 
r12  .  .  .  .  .  .  .  .  .  .  .  .  . 
r13  .  .  .  .  .  .  .  .  .  .  .  .  . 
r14  .  .  .  .  .  .  .  .  .  .  .  .  . 
r15  .  .  .  .  A  A  A  A  A  .  .  .  . 
r16  .  .  .  .  A  A  A  A  A  .  .  .  . 
r17  .  .  .  .  A  A  A  A  A  .  .  .  . 
r18  .  .  .  .  A  A  A  A  A  .  .  .  . 
r19  .  .  .  .  A  A  A  A  A  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  .  .  .  .  . 
```

---

## Tick 1 — Phase 1, Tick-in-phase 1

### State at tick start
- A: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(15,9) sp=0 f=(-1,+0)
  (0,1)→(15,10) sp=0 f=(-1,+0)
  (0,2)→(15,11) sp=0 f=(-1,+0)
  (0,3)→(15,12) sp=0 f=(-1,+0)
  (0,4)→(15,13) sp=0 f=(-1,+0)
  (1,0)→(16,9) sp=0 f=(-1,+0)
  (1,1)→(16,10) sp=0 f=(-1,+0)
  (1,2)→(16,11) sp=0 f=(-1,+0)
  (1,3)→(16,12) sp=0 f=(-1,+0)
  (1,4)→(16,13) sp=0 f=(-1,+0)
  (2,0)→(17,9) sp=0 f=(-1,+0)
  (2,1)→(17,10) sp=0 f=(-1,+0)
  (2,2)→(17,11) sp=0 f=(-1,+0)
  (2,3)→(17,12) sp=0 f=(-1,+0)
  (2,4)→(17,13) sp=0 f=(-1,+0)
  (3,0)→(18,9) sp=0 f=(-1,+0)
  (3,1)→(18,10) sp=0 f=(-1,+0)
  (3,2)→(18,11) sp=0 f=(-1,+0)
  (3,3)→(18,12) sp=0 f=(-1,+0)
  (3,4)→(18,13) sp=0 f=(-1,+0)
  (4,0)→(19,9) sp=0 f=(-1,+0)
  (4,1)→(19,10) sp=0 f=(-1,+0)
  (4,2)→(19,11) sp=0 f=(-1,+0)
  (4,3)→(19,12) sp=0 f=(-1,+0)
  (4,4)→(19,13) sp=0 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(9,9) sp=0 f=(+1,+0)
  (0,1)→(9,10) sp=0 f=(+1,+0)
  (0,2)→(9,11) sp=0 f=(+1,+0)
  (0,3)→(9,12) sp=0 f=(+1,+0)
  (0,4)→(9,13) sp=0 f=(+1,+0)
  (1,0)→(8,9) sp=0 f=(+1,+0)
  (1,1)→(8,10) sp=0 f=(+1,+0)
  (1,2)→(8,11) sp=0 f=(+1,+0)
  (1,3)→(8,12) sp=0 f=(+1,+0)
  (1,4)→(8,13) sp=0 f=(+1,+0)
  (2,0)→(7,9) sp=0 f=(+1,+0)
  (2,1)→(7,10) sp=0 f=(+1,+0)
  (2,2)→(7,11) sp=0 f=(+1,+0)
  (2,3)→(7,12) sp=0 f=(+1,+0)
  (2,4)→(7,13) sp=0 f=(+1,+0)
  (3,0)→(6,9) sp=0 f=(+1,+0)
  (3,1)→(6,10) sp=0 f=(+1,+0)
  (3,2)→(6,11) sp=0 f=(+1,+0)
  (3,3)→(6,12) sp=0 f=(+1,+0)
  (3,4)→(6,13) sp=0 f=(+1,+0)
  (4,0)→(5,9) sp=0 f=(+1,+0)
  (4,1)→(5,10) sp=0 f=(+1,+0)
  (4,2)→(5,11) sp=0 f=(+1,+0)
  (4,3)→(5,12) sp=0 f=(+1,+0)
  (4,4)→(5,13) sp=0 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 0 contact pair(s)

### Target assignment
- A targets: Line, centroid=(7.0, 11.0)
- B targets: Line, centroid=(17.0, 11.0)

### Advance phase
- A cells moved: 25
  - orig (0, 0): (15, 9) → (14, 9)
  - orig (0, 1): (15, 10) → (14, 10)
  - orig (0, 2): (15, 11) → (14, 11)
  - orig (0, 3): (15, 12) → (14, 12)
  - orig (0, 4): (15, 13) → (14, 13)
  - orig (1, 0): (16, 9) → (15, 9)
  - orig (1, 1): (16, 10) → (15, 10)
  - orig (1, 2): (16, 11) → (15, 11)
  ... +17 more
- B cells moved: 25
  - orig (0, 0): (9, 9) → (10, 9)
  - orig (0, 1): (9, 10) → (10, 10)
  - orig (0, 2): (9, 11) → (10, 11)
  - orig (0, 3): (9, 12) → (10, 12)
  - orig (0, 4): (9, 13) → (10, 13)
  - orig (1, 0): (8, 9) → (9, 9)
  - orig (1, 1): (8, 10) → (9, 10)
  - orig (1, 2): (8, 11) → (9, 11)
  ... +17 more

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 0 contact pair(s)

### Engagement pool components

### Engagement result
- A dmg taken: 0
- B dmg taken: 0
- engagements: 0

### End-of-tick deltas
- A: hp 20→20 (Δ0), sz 4→4 (Δ0), morale 6→6 (Δ0)
- B: hp 20→20 (Δ0), sz 4→4 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 6  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 7  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 8  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 9  .  .  .  .  B  B  B  B  B  .  .  .  . 
r10  .  .  .  .  B  B  B  B  B  .  .  .  . 
r11  .  .  .  .  .  .  .  .  .  .  .  .  . 
r12  .  .  .  .  .  .  .  .  .  .  .  .  . 
r13  .  .  .  .  .  .  .  .  .  .  .  .  . 
r14  .  .  .  .  A  A  A  A  A  .  .  .  . 
r15  .  .  .  .  A  A  A  A  A  .  .  .  . 
r16  .  .  .  .  A  A  A  A  A  .  .  .  . 
r17  .  .  .  .  A  A  A  A  A  .  .  .  . 
r18  .  .  .  .  A  A  A  A  A  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  .  .  .  .  . 
```

---

## Tick 2 — Phase 1, Tick-in-phase 2

### State at tick start
- A: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(14,9) sp=1 f=(-1,+0)
  (0,1)→(14,10) sp=1 f=(-1,+0)
  (0,2)→(14,11) sp=1 f=(-1,+0)
  (0,3)→(14,12) sp=1 f=(-1,+0)
  (0,4)→(14,13) sp=1 f=(-1,+0)
  (1,0)→(15,9) sp=1 f=(-1,+0)
  (1,1)→(15,10) sp=1 f=(-1,+0)
  (1,2)→(15,11) sp=1 f=(-1,+0)
  (1,3)→(15,12) sp=1 f=(-1,+0)
  (1,4)→(15,13) sp=1 f=(-1,+0)
  (2,0)→(16,9) sp=1 f=(-1,+0)
  (2,1)→(16,10) sp=1 f=(-1,+0)
  (2,2)→(16,11) sp=1 f=(-1,+0)
  (2,3)→(16,12) sp=1 f=(-1,+0)
  (2,4)→(16,13) sp=1 f=(-1,+0)
  (3,0)→(17,9) sp=1 f=(-1,+0)
  (3,1)→(17,10) sp=1 f=(-1,+0)
  (3,2)→(17,11) sp=1 f=(-1,+0)
  (3,3)→(17,12) sp=1 f=(-1,+0)
  (3,4)→(17,13) sp=1 f=(-1,+0)
  (4,0)→(18,9) sp=1 f=(-1,+0)
  (4,1)→(18,10) sp=1 f=(-1,+0)
  (4,2)→(18,11) sp=1 f=(-1,+0)
  (4,3)→(18,12) sp=1 f=(-1,+0)
  (4,4)→(18,13) sp=1 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(10,9) sp=1 f=(+1,+0)
  (0,1)→(10,10) sp=1 f=(+1,+0)
  (0,2)→(10,11) sp=1 f=(+1,+0)
  (0,3)→(10,12) sp=1 f=(+1,+0)
  (0,4)→(10,13) sp=1 f=(+1,+0)
  (1,0)→(9,9) sp=1 f=(+1,+0)
  (1,1)→(9,10) sp=1 f=(+1,+0)
  (1,2)→(9,11) sp=1 f=(+1,+0)
  (1,3)→(9,12) sp=1 f=(+1,+0)
  (1,4)→(9,13) sp=1 f=(+1,+0)
  (2,0)→(8,9) sp=1 f=(+1,+0)
  (2,1)→(8,10) sp=1 f=(+1,+0)
  (2,2)→(8,11) sp=1 f=(+1,+0)
  (2,3)→(8,12) sp=1 f=(+1,+0)
  (2,4)→(8,13) sp=1 f=(+1,+0)
  (3,0)→(7,9) sp=1 f=(+1,+0)
  (3,1)→(7,10) sp=1 f=(+1,+0)
  (3,2)→(7,11) sp=1 f=(+1,+0)
  (3,3)→(7,12) sp=1 f=(+1,+0)
  (3,4)→(7,13) sp=1 f=(+1,+0)
  (4,0)→(6,9) sp=1 f=(+1,+0)
  (4,1)→(6,10) sp=1 f=(+1,+0)
  (4,2)→(6,11) sp=1 f=(+1,+0)
  (4,3)→(6,12) sp=1 f=(+1,+0)
  (4,4)→(6,13) sp=1 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 0 contact pair(s)

### Target assignment
- A targets: Line, centroid=(8.0, 11.0)
- B targets: Line, centroid=(16.0, 11.0)

### Advance phase
- A cells moved: 25
  - orig (0, 0): (14, 9) → (13, 9)
  - orig (0, 1): (14, 10) → (13, 10)
  - orig (0, 2): (14, 11) → (13, 11)
  - orig (0, 3): (14, 12) → (13, 12)
  - orig (0, 4): (14, 13) → (13, 13)
  - orig (1, 0): (15, 9) → (14, 9)
  - orig (1, 1): (15, 10) → (14, 10)
  - orig (1, 2): (15, 11) → (14, 11)
  ... +17 more
- B cells moved: 25
  - orig (0, 0): (10, 9) → (11, 9)
  - orig (0, 1): (10, 10) → (11, 10)
  - orig (0, 2): (10, 11) → (11, 11)
  - orig (0, 3): (10, 12) → (11, 12)
  - orig (0, 4): (10, 13) → (11, 13)
  - orig (1, 0): (9, 9) → (10, 9)
  - orig (1, 1): (9, 10) → (10, 10)
  - orig (1, 2): (9, 11) → (10, 11)
  ... +17 more

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 0 contact pair(s)

### Engagement pool components

### Engagement result
- A dmg taken: 0
- B dmg taken: 0
- engagements: 0

### End-of-tick deltas
- A: hp 20→20 (Δ0), sz 4→4 (Δ0), morale 6→6 (Δ0)
- B: hp 20→20 (Δ0), sz 4→4 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 8  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 9  .  .  .  .  B  B  B  B  B  .  .  .  . 
r10  .  .  .  .  B  B  B  B  B  .  .  .  . 
r11  .  .  .  .  B  B  B  B  B  .  .  .  . 
r12  .  .  .  .  .  .  .  .  .  .  .  .  . 
r13  .  .  .  .  A  A  A  A  A  .  .  .  . 
r14  .  .  .  .  A  A  A  A  A  .  .  .  . 
r15  .  .  .  .  A  A  A  A  A  .  .  .  . 
r16  .  .  .  .  A  A  A  A  A  .  .  .  . 
r17  .  .  .  .  A  A  A  A  A  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  .  .  .  .  . 
```

---

## Tick 3 — Phase 1, Tick-in-phase 3

### State at tick start
- A: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(13,9) sp=1 f=(-1,+0)
  (0,1)→(13,10) sp=1 f=(-1,+0)
  (0,2)→(13,11) sp=1 f=(-1,+0)
  (0,3)→(13,12) sp=1 f=(-1,+0)
  (0,4)→(13,13) sp=1 f=(-1,+0)
  (1,0)→(14,9) sp=1 f=(-1,+0)
  (1,1)→(14,10) sp=1 f=(-1,+0)
  (1,2)→(14,11) sp=1 f=(-1,+0)
  (1,3)→(14,12) sp=1 f=(-1,+0)
  (1,4)→(14,13) sp=1 f=(-1,+0)
  (2,0)→(15,9) sp=1 f=(-1,+0)
  (2,1)→(15,10) sp=1 f=(-1,+0)
  (2,2)→(15,11) sp=1 f=(-1,+0)
  (2,3)→(15,12) sp=1 f=(-1,+0)
  (2,4)→(15,13) sp=1 f=(-1,+0)
  (3,0)→(16,9) sp=1 f=(-1,+0)
  (3,1)→(16,10) sp=1 f=(-1,+0)
  (3,2)→(16,11) sp=1 f=(-1,+0)
  (3,3)→(16,12) sp=1 f=(-1,+0)
  (3,4)→(16,13) sp=1 f=(-1,+0)
  (4,0)→(17,9) sp=1 f=(-1,+0)
  (4,1)→(17,10) sp=1 f=(-1,+0)
  (4,2)→(17,11) sp=1 f=(-1,+0)
  (4,3)→(17,12) sp=1 f=(-1,+0)
  (4,4)→(17,13) sp=1 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(11,9) sp=1 f=(+1,+0)
  (0,1)→(11,10) sp=1 f=(+1,+0)
  (0,2)→(11,11) sp=1 f=(+1,+0)
  (0,3)→(11,12) sp=1 f=(+1,+0)
  (0,4)→(11,13) sp=1 f=(+1,+0)
  (1,0)→(10,9) sp=1 f=(+1,+0)
  (1,1)→(10,10) sp=1 f=(+1,+0)
  (1,2)→(10,11) sp=1 f=(+1,+0)
  (1,3)→(10,12) sp=1 f=(+1,+0)
  (1,4)→(10,13) sp=1 f=(+1,+0)
  (2,0)→(9,9) sp=1 f=(+1,+0)
  (2,1)→(9,10) sp=1 f=(+1,+0)
  (2,2)→(9,11) sp=1 f=(+1,+0)
  (2,3)→(9,12) sp=1 f=(+1,+0)
  (2,4)→(9,13) sp=1 f=(+1,+0)
  (3,0)→(8,9) sp=1 f=(+1,+0)
  (3,1)→(8,10) sp=1 f=(+1,+0)
  (3,2)→(8,11) sp=1 f=(+1,+0)
  (3,3)→(8,12) sp=1 f=(+1,+0)
  (3,4)→(8,13) sp=1 f=(+1,+0)
  (4,0)→(7,9) sp=1 f=(+1,+0)
  (4,1)→(7,10) sp=1 f=(+1,+0)
  (4,2)→(7,11) sp=1 f=(+1,+0)
  (4,3)→(7,12) sp=1 f=(+1,+0)
  (4,4)→(7,13) sp=1 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 0 contact pair(s)

### Target assignment
- A targets: Line, centroid=(9.0, 11.0)
- B targets: Line, centroid=(15.0, 11.0)

### Advance phase
- A cells moved: 25
  - orig (0, 0): (13, 9) → (12, 9)
  - orig (0, 1): (13, 10) → (12, 10)
  - orig (0, 2): (13, 11) → (12, 11)
  - orig (0, 3): (13, 12) → (12, 12)
  - orig (0, 4): (13, 13) → (12, 13)
  - orig (1, 0): (14, 9) → (13, 9)
  - orig (1, 1): (14, 10) → (13, 10)
  - orig (1, 2): (14, 11) → (13, 11)
  ... +17 more
- B cells moved: 25
  - orig (0, 0): (11, 9) → (12, 9)
  - orig (0, 1): (11, 10) → (12, 10)
  - orig (0, 2): (11, 11) → (12, 11)
  - orig (0, 3): (11, 12) → (12, 12)
  - orig (0, 4): (11, 13) → (12, 13)
  - orig (1, 0): (10, 9) → (11, 9)
  - orig (1, 1): (10, 10) → (11, 10)
  - orig (1, 2): (10, 11) → (11, 11)
  ... +17 more

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[9, 10, 11, 12, 13]
    A contact cells (10): [(12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13)]
    B contact cells (10): [(11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13)]

### Engagement pool components
  - pair 0: primary_col=11
    A: role=normal off=0 base_pool=8 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00
    B: role=normal off=0 base_pool=8 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00

### Engagement result
- A dmg taken: 4
- B dmg taken: 0
- engagements: 1

### End-of-tick deltas
- A: hp 20→16 (Δ-4), sz 4→3 (Δ-1), morale 6→6 (Δ0)
- B: hp 20→20 (Δ0), sz 4→4 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  B  B  B  B  B  .  .  .  . 
r 9  .  .  .  .  B  B  B  B  B  .  .  .  . 
r10  .  .  .  .  B  B  B  B  B  .  .  .  . 
r11  .  .  .  .  B  B  B  B  B  .  .  .  . 
r12  .  .  .  .  #  #  #  #  #  .  .  .  . 
r13  .  .  .  .  A  A  A  A  A  .  .  .  . 
r14  .  .  .  .  A  A  A  A  A  .  .  .  . 
r15  .  .  .  .  A  A  A  A  A  .  .  .  . 
r16  .  .  .  .  A  A  A  A  A  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  .  .  .  .  . 
```

---

## Tick 4 — Phase 1, Tick-in-phase 4

### State at tick start
- A: hp=16/20, sz=3/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(-1,+0)
  (0,1)→(12,10) sp=1 f=(-1,+0)
  (0,2)→(12,11) sp=1 f=(-1,+0)
  (0,3)→(12,12) sp=1 f=(-1,+0)
  (0,4)→(12,13) sp=1 f=(-1,+0)
  (1,0)→(13,9) sp=1 f=(-1,+0)
  (1,1)→(13,10) sp=1 f=(-1,+0)
  (1,2)→(13,11) sp=1 f=(-1,+0)
  (1,3)→(13,12) sp=1 f=(-1,+0)
  (1,4)→(13,13) sp=1 f=(-1,+0)
  (2,0)→(14,9) sp=1 f=(-1,+0)
  (2,1)→(14,10) sp=1 f=(-1,+0)
  (2,2)→(14,11) sp=1 f=(-1,+0)
  (2,3)→(14,12) sp=1 f=(-1,+0)
  (2,4)→(14,13) sp=1 f=(-1,+0)
  (3,0)→(15,9) sp=1 f=(-1,+0)
  (3,1)→(15,10) sp=1 f=(-1,+0)
  (3,2)→(15,11) sp=1 f=(-1,+0)
  (3,3)→(15,12) sp=1 f=(-1,+0)
  (3,4)→(15,13) sp=1 f=(-1,+0)
  (4,0)→(16,9) sp=1 f=(-1,+0)
  (4,1)→(16,10) sp=1 f=(-1,+0)
  (4,2)→(16,11) sp=1 f=(-1,+0)
  (4,3)→(16,12) sp=1 f=(-1,+0)
  (4,4)→(16,13) sp=1 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(+1,+0)
  (0,1)→(12,10) sp=1 f=(+1,+0)
  (0,2)→(12,11) sp=1 f=(+1,+0)
  (0,3)→(12,12) sp=1 f=(+1,+0)
  (0,4)→(12,13) sp=1 f=(+1,+0)
  (1,0)→(11,9) sp=1 f=(+1,+0)
  (1,1)→(11,10) sp=1 f=(+1,+0)
  (1,2)→(11,11) sp=1 f=(+1,+0)
  (1,3)→(11,12) sp=1 f=(+1,+0)
  (1,4)→(11,13) sp=1 f=(+1,+0)
  (2,0)→(10,9) sp=1 f=(+1,+0)
  (2,1)→(10,10) sp=1 f=(+1,+0)
  (2,2)→(10,11) sp=1 f=(+1,+0)
  (2,3)→(10,12) sp=1 f=(+1,+0)
  (2,4)→(10,13) sp=1 f=(+1,+0)
  (3,0)→(9,9) sp=1 f=(+1,+0)
  (3,1)→(9,10) sp=1 f=(+1,+0)
  (3,2)→(9,11) sp=1 f=(+1,+0)
  (3,3)→(9,12) sp=1 f=(+1,+0)
  (3,4)→(9,13) sp=1 f=(+1,+0)
  (4,0)→(8,9) sp=1 f=(+1,+0)
  (4,1)→(8,10) sp=1 f=(+1,+0)
  (4,2)→(8,11) sp=1 f=(+1,+0)
  (4,3)→(8,12) sp=1 f=(+1,+0)
  (4,4)→(8,13) sp=1 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], cols=[9, 10, 11, 12, 13]

### Target assignment
- A targets: Line, centroid=(10.0, 11.0)
- B targets: Line, centroid=(14.0, 11.0)

### Advance phase
- A cells moved: 15
  - orig (2, 0): (14, 9) → (13, 9)
  - orig (2, 1): (14, 10) → (13, 10)
  - orig (2, 2): (14, 11) → (13, 11)
  - orig (2, 3): (14, 12) → (13, 12)
  - orig (2, 4): (14, 13) → (13, 13)
  - orig (3, 0): (15, 9) → (14, 9)
  - orig (3, 1): (15, 10) → (14, 10)
  - orig (3, 2): (15, 11) → (14, 11)
  ... +7 more
- B cells moved: 15
  - orig (2, 0): (10, 9) → (11, 9)
  - orig (2, 1): (10, 10) → (11, 10)
  - orig (2, 2): (10, 11) → (11, 11)
  - orig (2, 3): (10, 12) → (11, 12)
  - orig (2, 4): (10, 13) → (11, 13)
  - orig (3, 0): (9, 9) → (10, 9)
  - orig (3, 1): (9, 10) → (10, 10)
  - orig (3, 2): (9, 11) → (10, 11)
  ... +7 more

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[9, 10, 11, 12, 13]
    A contact cells (10): [(12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13)]
    B contact cells (10): [(11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13)]

### Engagement pool components
  - pair 0: primary_col=11
    A: role=normal off=0 base_pool=7 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00
    B: role=normal off=0 base_pool=8 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00

### Engagement result
- A dmg taken: 3
- B dmg taken: 0
- engagements: 1

### End-of-tick deltas
- A: hp 16→13 (Δ-3), sz 3→2 (Δ-1), morale 6→6 (Δ0)
- B: hp 20→20 (Δ0), sz 4→4 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  B  B  B  B  B  .  .  .  . 
r10  .  .  .  .  B  B  B  B  B  .  .  .  . 
r11  .  .  .  .  B  B  B  B  B  .  .  .  . 
r12  .  .  .  .  #  #  #  #  #  .  .  .  . 
r13  .  .  .  .  A  A  A  A  A  .  .  .  . 
r14  .  .  .  .  A  A  A  A  A  .  .  .  . 
r15  .  .  .  .  A  A  A  A  A  .  .  .  . 
r16  .  .  .  .  .  .  .  .  .  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  .  .  .  .  . 
```

---

## Tick 5 — Phase 1, Tick-in-phase 5

### State at tick start
- A: hp=13/20, sz=2/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(-1,+0) [HALT]
  (0,1)→(12,10) sp=1 f=(-1,+0) [HALT]
  (0,2)→(12,11) sp=1 f=(-1,+0) [HALT]
  (0,3)→(12,12) sp=1 f=(-1,+0) [HALT]
  (0,4)→(12,13) sp=1 f=(-1,+0) [HALT]
  (1,0)→(13,9) sp=1 f=(-1,+0) [HALT]
  (1,1)→(13,10) sp=1 f=(-1,+0) [HALT]
  (1,2)→(13,11) sp=1 f=(-1,+0) [HALT]
  (1,3)→(13,12) sp=1 f=(-1,+0) [HALT]
  (1,4)→(13,13) sp=1 f=(-1,+0) [HALT]
  (2,0)→(13,9) sp=1 f=(-1,+0)
  (2,1)→(13,10) sp=1 f=(-1,+0)
  (2,2)→(13,11) sp=1 f=(-1,+0)
  (2,3)→(13,12) sp=1 f=(-1,+0)
  (2,4)→(13,13) sp=1 f=(-1,+0)
  (3,0)→(14,9) sp=1 f=(-1,+0)
  (3,1)→(14,10) sp=1 f=(-1,+0)
  (3,2)→(14,11) sp=1 f=(-1,+0)
  (3,3)→(14,12) sp=1 f=(-1,+0)
  (3,4)→(14,13) sp=1 f=(-1,+0)
  (4,0)→(15,9) sp=1 f=(-1,+0)
  (4,1)→(15,10) sp=1 f=(-1,+0)
  (4,2)→(15,11) sp=1 f=(-1,+0)
  (4,3)→(15,12) sp=1 f=(-1,+0)
  (4,4)→(15,13) sp=1 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(+1,+0) [HALT]
  (0,1)→(12,10) sp=1 f=(+1,+0) [HALT]
  (0,2)→(12,11) sp=1 f=(+1,+0) [HALT]
  (0,3)→(12,12) sp=1 f=(+1,+0) [HALT]
  (0,4)→(12,13) sp=1 f=(+1,+0) [HALT]
  (1,0)→(11,9) sp=1 f=(+1,+0) [HALT]
  (1,1)→(11,10) sp=1 f=(+1,+0) [HALT]
  (1,2)→(11,11) sp=1 f=(+1,+0) [HALT]
  (1,3)→(11,12) sp=1 f=(+1,+0) [HALT]
  (1,4)→(11,13) sp=1 f=(+1,+0) [HALT]
  (2,0)→(11,9) sp=1 f=(+1,+0)
  (2,1)→(11,10) sp=1 f=(+1,+0)
  (2,2)→(11,11) sp=1 f=(+1,+0)
  (2,3)→(11,12) sp=1 f=(+1,+0)
  (2,4)→(11,13) sp=1 f=(+1,+0)
  (3,0)→(10,9) sp=1 f=(+1,+0)
  (3,1)→(10,10) sp=1 f=(+1,+0)
  (3,2)→(10,11) sp=1 f=(+1,+0)
  (3,3)→(10,12) sp=1 f=(+1,+0)
  (3,4)→(10,13) sp=1 f=(+1,+0)
  (4,0)→(9,9) sp=1 f=(+1,+0)
  (4,1)→(9,10) sp=1 f=(+1,+0)
  (4,2)→(9,11) sp=1 f=(+1,+0)
  (4,3)→(9,12) sp=1 f=(+1,+0)
  (4,4)→(9,13) sp=1 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], cols=[9, 10, 11, 12, 13]

### Target assignment
- A targets: Line, centroid=(10.6, 11.0)
- B targets: Line, centroid=(13.4, 11.0)

### Advance phase
- A cells moved: 15
  - orig (2, 0): (13, 9) → (12, 9)
  - orig (2, 1): (13, 10) → (12, 10)
  - orig (2, 2): (13, 11) → (12, 11)
  - orig (2, 3): (13, 12) → (12, 12)
  - orig (2, 4): (13, 13) → (12, 13)
  - orig (3, 0): (14, 9) → (13, 9)
  - orig (3, 1): (14, 10) → (13, 10)
  - orig (3, 2): (14, 11) → (13, 11)
  ... +7 more
- B cells moved: 15
  - orig (2, 0): (11, 9) → (12, 9)
  - orig (2, 1): (11, 10) → (12, 10)
  - orig (2, 2): (11, 11) → (12, 11)
  - orig (2, 3): (11, 12) → (12, 12)
  - orig (2, 4): (11, 13) → (12, 13)
  - orig (3, 0): (10, 9) → (11, 9)
  - orig (3, 1): (10, 10) → (11, 10)
  - orig (3, 2): (10, 11) → (11, 11)
  ... +7 more

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[9, 10, 11, 12, 13]
    A contact cells (10): [(12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13)]
    B contact cells (10): [(11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13)]

### Engagement pool components
  - pair 0: primary_col=11
    A: role=normal off=0 base_pool=6 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00
    B: role=normal off=0 base_pool=8 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00

### Engagement result
- A dmg taken: 0
- B dmg taken: 4
- engagements: 1

### End-of-tick deltas
- A: hp 13→13 (Δ0), sz 2→2 (Δ0), morale 6→6 (Δ0)
- B: hp 20→16 (Δ-4), sz 4→3 (Δ-1), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  .  B  B  B  B  B  .  .  .  . 
r11  .  .  .  .  B  B  B  B  B  .  .  .  . 
r12  .  .  .  .  B  B  B  B  B  .  .  .  . 
r13  .  .  .  .  A  A  A  A  A  .  .  .  . 
r14  .  .  .  .  A  A  A  A  A  .  .  .  . 
r15  .  .  .  .  .  .  .  .  .  .  .  .  . 
r16  .  .  .  .  .  .  .  .  .  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  .  .  .  .  . 
```

---

## Tick 6 — Phase 1, Tick-in-phase 6

### State at tick start
- A: hp=13/20, sz=2/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=16/20, sz=3/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(-1,+0) [HALT]
  (0,1)→(12,10) sp=1 f=(-1,+0) [HALT]
  (0,2)→(12,11) sp=1 f=(-1,+0) [HALT]
  (0,3)→(12,12) sp=1 f=(-1,+0) [HALT]
  (0,4)→(12,13) sp=1 f=(-1,+0) [HALT]
  (1,0)→(13,9) sp=1 f=(-1,+0) [HALT]
  (1,1)→(13,10) sp=1 f=(-1,+0) [HALT]
  (1,2)→(13,11) sp=1 f=(-1,+0) [HALT]
  (1,3)→(13,12) sp=1 f=(-1,+0) [HALT]
  (1,4)→(13,13) sp=1 f=(-1,+0) [HALT]
  (2,0)→(12,9) sp=1 f=(-1,+0)
  (2,1)→(12,10) sp=1 f=(-1,+0)
  (2,2)→(12,11) sp=1 f=(-1,+0)
  (2,3)→(12,12) sp=1 f=(-1,+0)
  (2,4)→(12,13) sp=1 f=(-1,+0)
  (3,0)→(13,9) sp=1 f=(-1,+0)
  (3,1)→(13,10) sp=1 f=(-1,+0)
  (3,2)→(13,11) sp=1 f=(-1,+0)
  (3,3)→(13,12) sp=1 f=(-1,+0)
  (3,4)→(13,13) sp=1 f=(-1,+0)
  (4,0)→(14,9) sp=1 f=(-1,+0)
  (4,1)→(14,10) sp=1 f=(-1,+0)
  (4,2)→(14,11) sp=1 f=(-1,+0)
  (4,3)→(14,12) sp=1 f=(-1,+0)
  (4,4)→(14,13) sp=1 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(+1,+0) [HALT]
  (0,1)→(12,10) sp=1 f=(+1,+0) [HALT]
  (0,2)→(12,11) sp=1 f=(+1,+0) [HALT]
  (0,3)→(12,12) sp=1 f=(+1,+0) [HALT]
  (0,4)→(12,13) sp=1 f=(+1,+0) [HALT]
  (1,0)→(11,9) sp=1 f=(+1,+0) [HALT]
  (1,1)→(11,10) sp=1 f=(+1,+0) [HALT]
  (1,2)→(11,11) sp=1 f=(+1,+0) [HALT]
  (1,3)→(11,12) sp=1 f=(+1,+0) [HALT]
  (1,4)→(11,13) sp=1 f=(+1,+0) [HALT]
  (2,0)→(12,9) sp=1 f=(+1,+0)
  (2,1)→(12,10) sp=1 f=(+1,+0)
  (2,2)→(12,11) sp=1 f=(+1,+0)
  (2,3)→(12,12) sp=1 f=(+1,+0)
  (2,4)→(12,13) sp=1 f=(+1,+0)
  (3,0)→(11,9) sp=1 f=(+1,+0)
  (3,1)→(11,10) sp=1 f=(+1,+0)
  (3,2)→(11,11) sp=1 f=(+1,+0)
  (3,3)→(11,12) sp=1 f=(+1,+0)
  (3,4)→(11,13) sp=1 f=(+1,+0)
  (4,0)→(10,9) sp=1 f=(+1,+0)
  (4,1)→(10,10) sp=1 f=(+1,+0)
  (4,2)→(10,11) sp=1 f=(+1,+0)
  (4,3)→(10,12) sp=1 f=(+1,+0)
  (4,4)→(10,13) sp=1 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], cols=[9, 10, 11, 12, 13]

### Target assignment
- A targets: Line, centroid=(11.2, 11.0)
- B targets: Line, centroid=(12.8, 11.0)

### Advance phase
- A cells moved: 15
  - orig (2, 0): (12, 9) → (11, 9)
  - orig (2, 1): (12, 10) → (11, 10)
  - orig (2, 2): (12, 11) → (11, 11)
  - orig (2, 3): (12, 12) → (11, 12)
  - orig (2, 4): (12, 13) → (11, 13)
  - orig (3, 0): (13, 9) → (12, 9)
  - orig (3, 1): (13, 10) → (12, 10)
  - orig (3, 2): (13, 11) → (12, 11)
  ... +7 more
- B cells moved: 10
  - orig (3, 0): (11, 9) → (12, 9)
  - orig (3, 1): (11, 10) → (12, 10)
  - orig (3, 2): (11, 11) → (12, 11)
  - orig (3, 3): (11, 12) → (12, 12)
  - orig (3, 4): (11, 13) → (12, 13)
  - orig (4, 0): (10, 9) → (11, 9)
  - orig (4, 1): (10, 10) → (11, 10)
  - orig (4, 2): (10, 11) → (11, 11)
  ... +2 more

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[9, 10, 11, 12, 13]
    A contact cells (15): [(11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13)]...
    B contact cells (10): [(11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13)]

### Engagement pool components
  - pair 0: primary_col=11
    A: role=normal off=0 base_pool=6 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00
    B: role=normal off=0 base_pool=7 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00

### Engagement result
- A dmg taken: 4
- B dmg taken: 0
- engagements: 1

### End-of-tick deltas
- A: hp 13→9 (Δ-4), sz 2→1 (Δ-1), morale 6→5 (Δ-1)
- B: hp 16→16 (Δ0), sz 3→3 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  .  .  .  .  .  .  .  .  .  . 
r11  .  .  .  .  B  B  B  B  B  .  .  .  . 
r12  .  .  .  .  B  B  B  B  B  .  .  .  . 
r13  .  .  .  .  A  A  A  A  A  .  .  .  . 
r14  .  .  .  .  .  .  .  .  .  .  .  .  . 
r15  .  .  .  .  .  .  .  .  .  .  .  .  . 
r16  .  .  .  .  .  .  .  .  .  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  .  .  .  .  . 
```

### ═══════ PHASE 1 BOUNDARY ═══════
- stamina_check fired (no-op in v14)
- morale_check_phase fired (no-op in v14)
- rout_resolution fired (no-op in v14)
- rally_check fired (no-op in v14)
- reform_check fired (no-op in v14)
- threadwork_check fired (no-op in v14)

---

## Tick 7 — Phase 2, Tick-in-phase 1

### State at tick start
- A: hp=9/20, sz=1/4, morale=5/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=16/20, sz=3/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(-1,+0) [HALT]
  (0,1)→(12,10) sp=1 f=(-1,+0) [HALT]
  (0,2)→(12,11) sp=1 f=(-1,+0) [HALT]
  (0,3)→(12,12) sp=1 f=(-1,+0) [HALT]
  (0,4)→(12,13) sp=1 f=(-1,+0) [HALT]
  (1,0)→(13,9) sp=1 f=(-1,+0) [HALT]
  (1,1)→(13,10) sp=1 f=(-1,+0) [HALT]
  (1,2)→(13,11) sp=1 f=(-1,+0) [HALT]
  (1,3)→(13,12) sp=1 f=(-1,+0) [HALT]
  (1,4)→(13,13) sp=1 f=(-1,+0) [HALT]
  (2,0)→(11,9) sp=1 f=(-1,+0)
  (2,1)→(11,10) sp=1 f=(-1,+0)
  (2,2)→(11,11) sp=1 f=(-1,+0)
  (2,3)→(11,12) sp=1 f=(-1,+0)
  (2,4)→(11,13) sp=1 f=(-1,+0)
  (3,0)→(12,9) sp=1 f=(-1,+0)
  (3,1)→(12,10) sp=1 f=(-1,+0)
  (3,2)→(12,11) sp=1 f=(-1,+0)
  (3,3)→(12,12) sp=1 f=(-1,+0)
  (3,4)→(12,13) sp=1 f=(-1,+0)
  (4,0)→(13,9) sp=1 f=(-1,+0)
  (4,1)→(13,10) sp=1 f=(-1,+0)
  (4,2)→(13,11) sp=1 f=(-1,+0)
  (4,3)→(13,12) sp=1 f=(-1,+0)
  (4,4)→(13,13) sp=1 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(+1,+0) [HALT]
  (0,1)→(12,10) sp=1 f=(+1,+0) [HALT]
  (0,2)→(12,11) sp=1 f=(+1,+0) [HALT]
  (0,3)→(12,12) sp=1 f=(+1,+0) [HALT]
  (0,4)→(12,13) sp=1 f=(+1,+0) [HALT]
  (1,0)→(11,9) sp=1 f=(+1,+0) [HALT]
  (1,1)→(11,10) sp=1 f=(+1,+0) [HALT]
  (1,2)→(11,11) sp=1 f=(+1,+0) [HALT]
  (1,3)→(11,12) sp=1 f=(+1,+0) [HALT]
  (1,4)→(11,13) sp=1 f=(+1,+0) [HALT]
  (2,0)→(12,9) sp=1 f=(+1,+0)
  (2,1)→(12,10) sp=1 f=(+1,+0)
  (2,2)→(12,11) sp=1 f=(+1,+0)
  (2,3)→(12,12) sp=1 f=(+1,+0)
  (2,4)→(12,13) sp=1 f=(+1,+0)
  (3,0)→(12,9) sp=1 f=(+1,+0)
  (3,1)→(12,10) sp=1 f=(+1,+0)
  (3,2)→(12,11) sp=1 f=(+1,+0)
  (3,3)→(12,12) sp=1 f=(+1,+0)
  (3,4)→(12,13) sp=1 f=(+1,+0)
  (4,0)→(11,9) sp=1 f=(+1,+0)
  (4,1)→(11,10) sp=1 f=(+1,+0)
  (4,2)→(11,11) sp=1 f=(+1,+0)
  (4,3)→(11,12) sp=1 f=(+1,+0)
  (4,4)→(11,13) sp=1 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], cols=[9, 10, 11, 12, 13]

### Target assignment
- A targets: Line, centroid=(11.6, 11.0)
- B targets: Line, centroid=(12.2, 11.0)

### Advance phase
- A cells moved: 5
  - orig (4, 0): (13, 9) → (12, 9)
  - orig (4, 1): (13, 10) → (12, 10)
  - orig (4, 2): (13, 11) → (12, 11)
  - orig (4, 3): (13, 12) → (12, 12)
  - orig (4, 4): (13, 13) → (12, 13)
- B cells moved: 5
  - orig (4, 0): (11, 9) → (12, 9)
  - orig (4, 1): (11, 10) → (12, 10)
  - orig (4, 2): (11, 11) → (12, 11)
  - orig (4, 3): (11, 12) → (12, 12)
  - orig (4, 4): (11, 13) → (12, 13)

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[9, 10, 11, 12, 13]
    A contact cells (15): [(11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13)]...
    B contact cells (10): [(11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13)]

### Engagement pool components
  - pair 0: primary_col=11
    A: role=normal off=0 base_pool=5 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00
    B: role=normal off=0 base_pool=7 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00

### Engagement result
- A dmg taken: 4
- B dmg taken: 0
- engagements: 1

### End-of-tick deltas
- A: hp 9→5 (Δ-4), sz 1→1 (Δ0), morale 5→4 (Δ-1)
- B: hp 16→16 (Δ0), sz 3→3 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  .  .  .  .  .  .  .  .  .  . 
r11  .  .  .  .  #  #  #  #  #  .  .  .  . 
r12  .  .  .  .  B  B  B  B  B  .  .  .  . 
r13  .  .  .  .  A  A  A  A  A  .  .  .  . 
r14  .  .  .  .  .  .  .  .  .  .  .  .  . 
r15  .  .  .  .  .  .  .  .  .  .  .  .  . 
r16  .  .  .  .  .  .  .  .  .  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  .  .  .  .  . 
```

---

## Tick 8 — Phase 2, Tick-in-phase 2

### State at tick start
- A: hp=5/20, sz=1/4, morale=4/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=16/20, sz=3/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(-1,+0) [HALT]
  (0,1)→(12,10) sp=1 f=(-1,+0) [HALT]
  (0,2)→(12,11) sp=1 f=(-1,+0) [HALT]
  (0,3)→(12,12) sp=1 f=(-1,+0) [HALT]
  (0,4)→(12,13) sp=1 f=(-1,+0) [HALT]
  (1,0)→(13,9) sp=1 f=(-1,+0) [HALT]
  (1,1)→(13,10) sp=1 f=(-1,+0) [HALT]
  (1,2)→(13,11) sp=1 f=(-1,+0) [HALT]
  (1,3)→(13,12) sp=1 f=(-1,+0) [HALT]
  (1,4)→(13,13) sp=1 f=(-1,+0) [HALT]
  (2,0)→(11,9) sp=1 f=(-1,+0) [HALT]
  (2,1)→(11,10) sp=1 f=(-1,+0) [HALT]
  (2,2)→(11,11) sp=1 f=(-1,+0) [HALT]
  (2,3)→(11,12) sp=1 f=(-1,+0) [HALT]
  (2,4)→(11,13) sp=1 f=(-1,+0) [HALT]
  (3,0)→(12,9) sp=1 f=(-1,+0)
  (3,1)→(12,10) sp=1 f=(-1,+0)
  (3,2)→(12,11) sp=1 f=(-1,+0)
  (3,3)→(12,12) sp=1 f=(-1,+0)
  (3,4)→(12,13) sp=1 f=(-1,+0)
  (4,0)→(12,9) sp=1 f=(-1,+0)
  (4,1)→(12,10) sp=1 f=(-1,+0)
  (4,2)→(12,11) sp=1 f=(-1,+0)
  (4,3)→(12,12) sp=1 f=(-1,+0)
  (4,4)→(12,13) sp=1 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,9) sp=1 f=(+1,+0) [HALT]
  (0,1)→(12,10) sp=1 f=(+1,+0) [HALT]
  (0,2)→(12,11) sp=1 f=(+1,+0) [HALT]
  (0,3)→(12,12) sp=1 f=(+1,+0) [HALT]
  (0,4)→(12,13) sp=1 f=(+1,+0) [HALT]
  (1,0)→(11,9) sp=1 f=(+1,+0) [HALT]
  (1,1)→(11,10) sp=1 f=(+1,+0) [HALT]
  (1,2)→(11,11) sp=1 f=(+1,+0) [HALT]
  (1,3)→(11,12) sp=1 f=(+1,+0) [HALT]
  (1,4)→(11,13) sp=1 f=(+1,+0) [HALT]
  (2,0)→(12,9) sp=1 f=(+1,+0)
  (2,1)→(12,10) sp=1 f=(+1,+0)
  (2,2)→(12,11) sp=1 f=(+1,+0)
  (2,3)→(12,12) sp=1 f=(+1,+0)
  (2,4)→(12,13) sp=1 f=(+1,+0)
  (3,0)→(12,9) sp=1 f=(+1,+0)
  (3,1)→(12,10) sp=1 f=(+1,+0)
  (3,2)→(12,11) sp=1 f=(+1,+0)
  (3,3)→(12,12) sp=1 f=(+1,+0)
  (3,4)→(12,13) sp=1 f=(+1,+0)
  (4,0)→(12,9) sp=1 f=(+1,+0)
  (4,1)→(12,10) sp=1 f=(+1,+0)
  (4,2)→(12,11) sp=1 f=(+1,+0)
  (4,3)→(12,12) sp=1 f=(+1,+0)
  (4,4)→(12,13) sp=1 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], cols=[9, 10, 11, 12, 13]

### Target assignment
- A targets: Line, centroid=(11.8, 11.0)
- B targets: Line, centroid=(12.0, 11.0)

### Advance phase
- A cells moved: 0
- B cells moved: 0

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[9, 10, 11, 12, 13]
    A contact cells (15): [(11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13)]...
    B contact cells (10): [(11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13)]

### Engagement pool components
  - pair 0: primary_col=11
    A: role=normal off=0 base_pool=5 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00
    B: role=normal off=0 base_pool=7 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.00

### Engagement result
- A dmg taken: 4
- B dmg taken: 0
- engagements: 1

### End-of-tick deltas
- A: hp 5→1 (Δ-4), sz 1→0 (Δ-1), morale 4→4 (Δ0)
- B: hp 16→16 (Δ0), sz 3→3 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  .  .  .  .  .  .  .  .  .  . 
r11  .  .  .  .  #  #  #  #  #  .  .  .  . 
r12  .  .  .  .  B  B  B  B  B  .  .  .  . 
r13  .  .  .  .  A  A  A  A  A  .  .  .  . 
r14  .  .  .  .  .  .  .  .  .  .  .  .  . 
r15  .  .  .  .  .  .  .  .  .  .  .  .  . 
r16  .  .  .  .  .  .  .  .  .  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  .  .  .  .  . 
```

---

## Tick 9 — Phase 2, Tick-in-phase 3

**Battle ended:** A.routed=True, B.routed=False
---

## Battle result

- Winner: **B**
- Turns: 9
- Phases completed: 1
- Final A: hp=1/20, sz=0/4, routed=True
- Final B: hp=16/20, sz=3/4, routed=False
