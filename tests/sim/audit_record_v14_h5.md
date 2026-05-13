# SIM-MB-06 Tick-by-Tick Record

**Seed:** 1000000  **Max turns:** 15  **TICKS_PER_PHASE:** 6

## Initial state

- A: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
  - subunit: shape=RefusedFlank, tier=3, start=(15, 9), advance_dir=-1, unit_type=melee
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
  - subunit: shape=Horseshoe, tier=3, start=(5, 8), advance_dir=1, unit_type=melee

### Initial grid
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  B  B  B  B  B  B  B  .  .  . 
r 6  .  .  .  B  B  B  .  B  B  B  .  .  . 
r 7  .  .  .  B  B  B  .  B  B  B  .  .  . 
r 8  .  .  .  B  B  B  .  B  B  B  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  .  .  .  .  .  .  .  .  .  . 
r11  .  .  .  .  .  .  .  .  .  .  .  .  . 
r12  .  .  .  .  .  .  .  .  .  .  .  .  . 
r13  .  .  .  .  .  .  .  .  .  .  .  .  . 
r14  .  .  .  .  .  .  .  .  .  .  .  .  . 
r15  .  .  .  .  A  A  A  A  .  .  .  .  . 
r16  .  .  .  .  A  A  A  A  .  .  .  .  . 
r17  .  .  .  .  A  A  A  A  .  .  .  .  . 
r18  .  .  .  .  A  A  A  A  .  .  .  .  . 
r19  .  .  .  .  A  A  A  A  .  .  .  .  . 
r20  .  .  .  .  A  A  A  A  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  A  .  .  .  . 
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
  (1,0)→(16,9) sp=0 f=(-1,+0)
  (1,1)→(16,10) sp=0 f=(-1,+0)
  (1,2)→(16,11) sp=0 f=(-1,+0)
  (1,3)→(16,12) sp=0 f=(-1,+0)
  (2,0)→(17,9) sp=0 f=(-1,+0)
  (2,1)→(17,10) sp=0 f=(-1,+0)
  (2,2)→(17,11) sp=0 f=(-1,+0)
  (2,3)→(17,12) sp=0 f=(-1,+0)
  (3,0)→(18,9) sp=0 f=(-1,+0)
  (3,1)→(18,10) sp=0 f=(-1,+0)
  (3,2)→(18,11) sp=0 f=(-1,+0)
  (3,3)→(18,12) sp=0 f=(-1,+0)
  (4,0)→(19,9) sp=0 f=(-1,+0)
  (4,1)→(19,10) sp=0 f=(-1,+0)
  (4,2)→(19,11) sp=0 f=(-1,+0)
  (4,3)→(19,12) sp=0 f=(-1,+0)
  (5,0)→(20,9) sp=0 f=(-1,+0)
  (5,1)→(20,10) sp=0 f=(-1,+0)
  (5,2)→(20,11) sp=0 f=(-1,+0)
  (5,3)→(20,12) sp=0 f=(-1,+0)
  (6,4)→(21,13) sp=0 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(8,8) sp=0 f=(+1,+0)
  (0,1)→(8,9) sp=0 f=(+1,+0)
  (0,2)→(8,10) sp=0 f=(+1,+0)
  (0,4)→(8,12) sp=0 f=(+1,+0)
  (0,5)→(8,13) sp=0 f=(+1,+0)
  (0,6)→(8,14) sp=0 f=(+1,+0)
  (1,0)→(7,8) sp=0 f=(+1,+0)
  (1,1)→(7,9) sp=0 f=(+1,+0)
  (1,2)→(7,10) sp=0 f=(+1,+0)
  (1,4)→(7,12) sp=0 f=(+1,+0)
  (1,5)→(7,13) sp=0 f=(+1,+0)
  (1,6)→(7,14) sp=0 f=(+1,+0)
  (2,0)→(6,8) sp=0 f=(+1,+0)
  (2,1)→(6,9) sp=0 f=(+1,+0)
  (2,2)→(6,10) sp=0 f=(+1,+0)
  (2,4)→(6,12) sp=0 f=(+1,+0)
  (2,5)→(6,13) sp=0 f=(+1,+0)
  (2,6)→(6,14) sp=0 f=(+1,+0)
  (3,0)→(5,8) sp=0 f=(+1,+0)
  (3,1)→(5,9) sp=0 f=(+1,+0)
  (3,2)→(5,10) sp=0 f=(+1,+0)
  (3,3)→(5,11) sp=0 f=(+1,+0)
  (3,4)→(5,12) sp=0 f=(+1,+0)
  (3,5)→(5,13) sp=0 f=(+1,+0)
  (3,6)→(5,14) sp=0 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 0 contact pair(s)

### Target assignment
- A targets: RefusedFlank, centroid=(6.44, 11.0)
- B targets: Horseshoe, centroid=(17.64, 10.6)

### Advance phase
- A cells moved: 24
  - orig (0, 0): (15, 9) → (13, 9)
  - orig (0, 1): (15, 10) → (13, 10)
  - orig (0, 2): (15, 11) → (13, 11)
  - orig (0, 3): (15, 12) → (13, 12)
  - orig (1, 0): (16, 9) → (15, 9)
  - orig (1, 1): (16, 10) → (15, 10)
  - orig (1, 2): (16, 11) → (15, 11)
  - orig (1, 3): (16, 12) → (15, 12)
  ... +16 more
- B cells moved: 18
  - orig (0, 0): (8, 8) → (10, 8)
  - orig (0, 1): (8, 9) → (10, 9)
  - orig (0, 2): (8, 10) → (10, 10)
  - orig (0, 4): (8, 12) → (10, 12)
  - orig (0, 5): (8, 13) → (10, 13)
  - orig (0, 6): (8, 14) → (10, 14)
  - orig (1, 0): (7, 8) → (9, 8)
  - orig (1, 1): (7, 9) → (9, 9)
  ... +10 more

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
r 5  .  .  .  B  B  B  B  B  B  B  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  B  B  B  .  B  B  B  .  .  . 
r 9  .  .  .  B  B  B  .  B  B  B  .  .  . 
r10  .  .  .  B  B  B  .  B  B  B  .  .  . 
r11  .  .  .  .  .  .  .  .  .  .  .  .  . 
r12  .  .  .  .  .  .  .  .  .  .  .  .  . 
r13  .  .  .  .  A  A  A  A  .  .  .  .  . 
r14  .  .  .  .  .  .  .  .  .  .  .  .  . 
r15  .  .  .  .  A  A  A  A  .  .  .  .  . 
r16  .  .  .  .  A  A  A  A  .  .  .  .  . 
r17  .  .  .  .  A  A  A  A  .  .  .  .  . 
r18  .  .  .  .  A  A  A  A  .  .  .  .  . 
r19  .  .  .  .  A  A  A  A  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  A  .  .  .  . 
```

---

## Tick 2 — Phase 1, Tick-in-phase 2

### State at tick start
- A: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(13,9) sp=2 f=(-2,+0)
  (0,1)→(13,10) sp=2 f=(-2,+0)
  (0,2)→(13,11) sp=2 f=(-2,+0)
  (0,3)→(13,12) sp=2 f=(-2,+0)
  (1,0)→(15,9) sp=1 f=(-1,+0)
  (1,1)→(15,10) sp=1 f=(-1,+0)
  (1,2)→(15,11) sp=1 f=(-1,+0)
  (1,3)→(15,12) sp=1 f=(-1,+0)
  (2,0)→(16,9) sp=1 f=(-1,+0)
  (2,1)→(16,10) sp=1 f=(-1,+0)
  (2,2)→(16,11) sp=1 f=(-1,+0)
  (2,3)→(16,12) sp=1 f=(-1,+0)
  (3,0)→(17,9) sp=1 f=(-1,+0)
  (3,1)→(17,10) sp=1 f=(-1,+0)
  (3,2)→(17,11) sp=1 f=(-1,+0)
  (3,3)→(17,12) sp=1 f=(-1,+0)
  (4,0)→(18,9) sp=1 f=(-1,+0)
  (4,1)→(18,10) sp=1 f=(-1,+0)
  (4,2)→(18,11) sp=1 f=(-1,+0)
  (4,3)→(18,12) sp=1 f=(-1,+0)
  (5,0)→(19,9) sp=1 f=(-1,+0)
  (5,1)→(19,10) sp=1 f=(-1,+0)
  (5,2)→(19,11) sp=1 f=(-1,+0)
  (5,3)→(19,12) sp=1 f=(-1,+0)
  (6,4)→(21,13) sp=0 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(10,8) sp=2 f=(+2,+0)
  (0,1)→(10,9) sp=2 f=(+2,+0)
  (0,2)→(10,10) sp=2 f=(+2,+0)
  (0,4)→(10,12) sp=2 f=(+2,+0)
  (0,5)→(10,13) sp=2 f=(+2,+0)
  (0,6)→(10,14) sp=2 f=(+2,+0)
  (1,0)→(9,8) sp=2 f=(+2,+0)
  (1,1)→(9,9) sp=2 f=(+2,+0)
  (1,2)→(9,10) sp=2 f=(+2,+0)
  (1,4)→(9,12) sp=2 f=(+2,+0)
  (1,5)→(9,13) sp=2 f=(+2,+0)
  (1,6)→(9,14) sp=2 f=(+2,+0)
  (2,0)→(8,8) sp=2 f=(+2,+0)
  (2,1)→(8,9) sp=2 f=(+2,+0)
  (2,2)→(8,10) sp=2 f=(+2,+0)
  (2,4)→(8,12) sp=2 f=(+2,+0)
  (2,5)→(8,13) sp=2 f=(+2,+0)
  (2,6)→(8,14) sp=2 f=(+2,+0)
  (3,0)→(5,8) sp=0 f=(+1,+0)
  (3,1)→(5,9) sp=0 f=(+1,+0)
  (3,2)→(5,10) sp=0 f=(+1,+0)
  (3,3)→(5,11) sp=0 f=(+1,+0)
  (3,4)→(5,12) sp=0 f=(+1,+0)
  (3,5)→(5,13) sp=0 f=(+1,+0)
  (3,6)→(5,14) sp=0 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 0 contact pair(s)

### Target assignment
- A targets: RefusedFlank, centroid=(7.88, 11.0)
- B targets: Horseshoe, centroid=(16.52, 10.6)

### Advance phase
- A cells moved: 24
  - orig (0, 0): (13, 9) → (11, 9)
  - orig (0, 1): (13, 10) → (11, 10)
  - orig (0, 2): (13, 11) → (11, 11)
  - orig (0, 3): (13, 12) → (11, 12)
  - orig (1, 0): (15, 9) → (14, 9)
  - orig (1, 1): (15, 10) → (14, 10)
  - orig (1, 2): (15, 11) → (14, 11)
  - orig (1, 3): (15, 12) → (14, 12)
  ... +16 more
- B cells moved: 18
  - orig (0, 0): (10, 8) → (12, 8)
  - orig (0, 1): (10, 9) → (12, 9)
  - orig (0, 2): (10, 10) → (12, 10)
  - orig (0, 4): (10, 12) → (12, 12)
  - orig (0, 5): (10, 13) → (12, 13)
  - orig (0, 6): (10, 14) → (12, 14)
  - orig (1, 0): (9, 8) → (11, 8)
  - orig (1, 1): (9, 9) → (11, 9)
  ... +10 more

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[8, 9, 10, 11, 12]
    A contact cells (4): [(11, 9), (11, 10), (11, 11), (11, 12)]
    B contact cells (15): [(10, 8), (10, 9), (10, 10), (10, 12), (10, 13), (11, 8), (11, 9), (11, 10), (11, 12), (11, 13)]...

### Engagement pool components
  - pair 0: primary_col=10
    A: role=engaged off=0 base_pool=8 troops_frac=1.00 engage_frac=1.00 momentum_speed=2.00
    B: role=flank_engaged off=0 base_pool=8 troops_frac=1.00 engage_frac=1.00 momentum_speed=2.00

### Engagement result
- A dmg taken: 3
- B dmg taken: 0
- engagements: 1

### End-of-tick deltas
- A: hp 20→17 (Δ-3), sz 4→3 (Δ-1), morale 6→6 (Δ0)
- B: hp 20→20 (Δ0), sz 4→4 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  B  B  B  B  B  B  B  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  B  B  B  .  B  B  B  .  .  . 
r11  .  .  .  B  #  #  A  #  B  B  .  .  . 
r12  .  .  .  B  B  B  .  B  B  B  .  .  . 
r13  .  .  .  .  .  .  .  .  .  .  .  .  . 
r14  .  .  .  .  A  A  A  A  .  .  .  .  . 
r15  .  .  .  .  A  A  A  A  .  .  .  .  . 
r16  .  .  .  .  A  A  A  A  .  .  .  .  . 
r17  .  .  .  .  A  A  A  A  .  .  .  .  . 
r18  .  .  .  .  A  A  A  A  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  A  .  .  .  . 
```

---

## Tick 3 — Phase 1, Tick-in-phase 3

### State at tick start
- A: hp=17/20, sz=3/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(11,9) sp=2 f=(-2,+0)
  (0,1)→(11,10) sp=2 f=(-2,+0)
  (0,2)→(11,11) sp=2 f=(-2,+0)
  (0,3)→(11,12) sp=2 f=(-2,+0)
  (1,0)→(14,9) sp=1 f=(-1,+0)
  (1,1)→(14,10) sp=1 f=(-1,+0)
  (1,2)→(14,11) sp=1 f=(-1,+0)
  (1,3)→(14,12) sp=1 f=(-1,+0)
  (2,0)→(15,9) sp=1 f=(-1,+0)
  (2,1)→(15,10) sp=1 f=(-1,+0)
  (2,2)→(15,11) sp=1 f=(-1,+0)
  (2,3)→(15,12) sp=1 f=(-1,+0)
  (3,0)→(16,9) sp=1 f=(-1,+0)
  (3,1)→(16,10) sp=1 f=(-1,+0)
  (3,2)→(16,11) sp=1 f=(-1,+0)
  (3,3)→(16,12) sp=1 f=(-1,+0)
  (4,0)→(17,9) sp=1 f=(-1,+0)
  (4,1)→(17,10) sp=1 f=(-1,+0)
  (4,2)→(17,11) sp=1 f=(-1,+0)
  (4,3)→(17,12) sp=1 f=(-1,+0)
  (5,0)→(18,9) sp=1 f=(-1,+0)
  (5,1)→(18,10) sp=1 f=(-1,+0)
  (5,2)→(18,11) sp=1 f=(-1,+0)
  (5,3)→(18,12) sp=1 f=(-1,+0)
  (6,4)→(21,13) sp=0 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,8) sp=2 f=(+2,+0)
  (0,1)→(12,9) sp=2 f=(+2,+0)
  (0,2)→(12,10) sp=2 f=(+2,+0)
  (0,4)→(12,12) sp=2 f=(+2,+0)
  (0,5)→(12,13) sp=2 f=(+2,+0)
  (0,6)→(12,14) sp=2 f=(+2,+0)
  (1,0)→(11,8) sp=2 f=(+2,+0)
  (1,1)→(11,9) sp=2 f=(+2,+0)
  (1,2)→(11,10) sp=2 f=(+2,+0)
  (1,4)→(11,12) sp=2 f=(+2,+0)
  (1,5)→(11,13) sp=2 f=(+2,+0)
  (1,6)→(11,14) sp=2 f=(+2,+0)
  (2,0)→(10,8) sp=2 f=(+2,+0)
  (2,1)→(10,9) sp=2 f=(+2,+0)
  (2,2)→(10,10) sp=2 f=(+2,+0)
  (2,4)→(10,12) sp=2 f=(+2,+0)
  (2,5)→(10,13) sp=2 f=(+2,+0)
  (2,6)→(10,14) sp=2 f=(+2,+0)
  (3,0)→(5,8) sp=0 f=(+1,+0)
  (3,1)→(5,9) sp=0 f=(+1,+0)
  (3,2)→(5,10) sp=0 f=(+1,+0)
  (3,3)→(5,11) sp=0 f=(+1,+0)
  (3,4)→(5,12) sp=0 f=(+1,+0)
  (3,5)→(5,13) sp=0 f=(+1,+0)
  (3,6)→(5,14) sp=0 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 4), (2, 5)], cols=[8, 9, 10, 11, 12]

### Target assignment
- A targets: RefusedFlank, centroid=(9.32, 11.0)
- B targets: Horseshoe, centroid=(15.4, 10.6)

### Advance phase
- A cells moved: 20
  - orig (1, 0): (14, 9) → (13, 9)
  - orig (1, 1): (14, 10) → (13, 10)
  - orig (1, 2): (14, 11) → (13, 11)
  - orig (1, 3): (14, 12) → (13, 12)
  - orig (2, 0): (15, 9) → (14, 9)
  - orig (2, 1): (15, 10) → (14, 10)
  - orig (2, 2): (15, 11) → (14, 11)
  - orig (2, 3): (15, 12) → (14, 12)
  ... +12 more
- B cells moved: 3
  - orig (0, 6): (12, 14) → (14, 14)
  - orig (1, 6): (11, 14) → (13, 14)
  - orig (2, 6): (10, 14) → (12, 14)

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[8, 9, 10, 11, 12]
    A contact cells (8): [(11, 9), (11, 10), (11, 11), (11, 12), (13, 9), (13, 10), (13, 11), (13, 12)]
    B contact cells (15): [(10, 8), (10, 9), (10, 10), (10, 12), (10, 13), (11, 8), (11, 9), (11, 10), (11, 12), (11, 13)]...

### Engagement pool components
  - pair 0: primary_col=10
    A: role=engaged off=0 base_pool=7 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.75
    B: role=flank_engaged off=0 base_pool=8 troops_frac=1.00 engage_frac=1.00 momentum_speed=2.00

### Engagement result
- A dmg taken: 4
- B dmg taken: 0
- engagements: 1

### End-of-tick deltas
- A: hp 17→13 (Δ-4), sz 3→2 (Δ-1), morale 6→6 (Δ0)
- B: hp 20→20 (Δ0), sz 4→4 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  B  B  B  B  B  B  B  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  B  B  B  .  B  B  .  .  .  . 
r11  .  .  .  B  #  #  A  #  B  .  .  .  . 
r12  .  .  .  B  B  B  .  B  B  B  .  .  . 
r13  .  .  .  .  A  A  A  A  .  B  .  .  . 
r14  .  .  .  .  A  A  A  A  .  B  .  .  . 
r15  .  .  .  .  A  A  A  A  .  .  .  .  . 
r16  .  .  .  .  A  A  A  A  .  .  .  .  . 
r17  .  .  .  .  A  A  A  A  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  A  .  .  .  . 
```

---

## Tick 4 — Phase 1, Tick-in-phase 4

### State at tick start
- A: hp=13/20, sz=2/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=20/20, sz=4/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(11,9) sp=2 f=(-2,+0) [HALT]
  (0,1)→(11,10) sp=2 f=(-2,+0) [HALT]
  (0,2)→(11,11) sp=2 f=(-2,+0) [HALT]
  (0,3)→(11,12) sp=2 f=(-2,+0) [HALT]
  (1,0)→(13,9) sp=1 f=(-1,+0)
  (1,1)→(13,10) sp=1 f=(-1,+0)
  (1,2)→(13,11) sp=1 f=(-1,+0)
  (1,3)→(13,12) sp=1 f=(-1,+0)
  (2,0)→(14,9) sp=1 f=(-1,+0)
  (2,1)→(14,10) sp=1 f=(-1,+0)
  (2,2)→(14,11) sp=1 f=(-1,+0)
  (2,3)→(14,12) sp=1 f=(-1,+0)
  (3,0)→(15,9) sp=1 f=(-1,+0)
  (3,1)→(15,10) sp=1 f=(-1,+0)
  (3,2)→(15,11) sp=1 f=(-1,+0)
  (3,3)→(15,12) sp=1 f=(-1,+0)
  (4,0)→(16,9) sp=1 f=(-1,+0)
  (4,1)→(16,10) sp=1 f=(-1,+0)
  (4,2)→(16,11) sp=1 f=(-1,+0)
  (4,3)→(16,12) sp=1 f=(-1,+0)
  (5,0)→(17,9) sp=1 f=(-1,+0)
  (5,1)→(17,10) sp=1 f=(-1,+0)
  (5,2)→(17,11) sp=1 f=(-1,+0)
  (5,3)→(17,12) sp=1 f=(-1,+0)
  (6,4)→(21,13) sp=0 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,8) sp=2 f=(+2,+0) [HALT]
  (0,1)→(12,9) sp=2 f=(+2,+0) [HALT]
  (0,2)→(12,10) sp=2 f=(+2,+0) [HALT]
  (0,4)→(12,12) sp=2 f=(+2,+0) [HALT]
  (0,5)→(12,13) sp=2 f=(+2,+0) [HALT]
  (0,6)→(14,14) sp=2 f=(+2,+0)
  (1,0)→(11,8) sp=2 f=(+2,+0) [HALT]
  (1,1)→(11,9) sp=2 f=(+2,+0) [HALT]
  (1,2)→(11,10) sp=2 f=(+2,+0) [HALT]
  (1,4)→(11,12) sp=2 f=(+2,+0) [HALT]
  (1,5)→(11,13) sp=2 f=(+2,+0) [HALT]
  (1,6)→(13,14) sp=2 f=(+2,+0)
  (2,0)→(10,8) sp=2 f=(+2,+0) [HALT]
  (2,1)→(10,9) sp=2 f=(+2,+0) [HALT]
  (2,2)→(10,10) sp=2 f=(+2,+0) [HALT]
  (2,4)→(10,12) sp=2 f=(+2,+0) [HALT]
  (2,5)→(10,13) sp=2 f=(+2,+0) [HALT]
  (2,6)→(12,14) sp=2 f=(+2,+0)
  (3,0)→(5,8) sp=0 f=(+1,+0)
  (3,1)→(5,9) sp=0 f=(+1,+0)
  (3,2)→(5,10) sp=0 f=(+1,+0)
  (3,3)→(5,11) sp=0 f=(+1,+0)
  (3,4)→(5,12) sp=0 f=(+1,+0)
  (3,5)→(5,13) sp=0 f=(+1,+0)
  (3,6)→(5,14) sp=0 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 4), (2, 5)], cols=[8, 9, 10, 11, 12]

### Target assignment
- A targets: RefusedFlank, centroid=(9.56, 11.0)
- B targets: Horseshoe, centroid=(14.6, 10.6)

### Advance phase
- A cells moved: 16
  - orig (2, 0): (14, 9) → (13, 9)
  - orig (2, 1): (14, 10) → (13, 10)
  - orig (2, 2): (14, 11) → (13, 11)
  - orig (2, 3): (14, 12) → (13, 12)
  - orig (3, 0): (15, 9) → (14, 9)
  - orig (3, 1): (15, 10) → (14, 10)
  - orig (3, 2): (15, 11) → (14, 11)
  - orig (3, 3): (15, 12) → (14, 12)
  ... +8 more
- B cells moved: 2
  - orig (1, 6): (13, 14) → (15, 14)
  - orig (2, 6): (12, 14) → (14, 14)

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[8, 9, 10, 11, 12]
    A contact cells (8): [(11, 9), (11, 10), (11, 11), (11, 12), (13, 9), (13, 10), (13, 11), (13, 12)]
    B contact cells (15): [(10, 8), (10, 9), (10, 10), (10, 12), (10, 13), (11, 8), (11, 9), (11, 10), (11, 12), (11, 13)]...

### Engagement pool components
  - pair 0: primary_col=10
    A: role=engaged off=0 base_pool=6 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.75
    B: role=flank_engaged off=0 base_pool=8 troops_frac=1.00 engage_frac=1.00 momentum_speed=2.00

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
r 5  .  .  .  B  B  B  B  B  B  B  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  B  B  B  .  B  B  .  .  .  . 
r11  .  .  .  B  #  #  A  #  B  .  .  .  . 
r12  .  .  .  B  B  B  .  B  B  .  .  .  . 
r13  .  .  .  .  A  A  A  A  .  .  .  .  . 
r14  .  .  .  .  A  A  A  A  .  B  .  .  . 
r15  .  .  .  .  A  A  A  A  .  B  .  .  . 
r16  .  .  .  .  A  A  A  A  .  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  A  .  .  .  . 
```

---

## Tick 5 — Phase 1, Tick-in-phase 5

### State at tick start
- A: hp=13/20, sz=2/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=16/20, sz=3/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(11,9) sp=2 f=(-2,+0) [HALT]
  (0,1)→(11,10) sp=2 f=(-2,+0) [HALT]
  (0,2)→(11,11) sp=2 f=(-2,+0) [HALT]
  (0,3)→(11,12) sp=2 f=(-2,+0) [HALT]
  (1,0)→(13,9) sp=1 f=(-1,+0) [HALT]
  (1,1)→(13,10) sp=1 f=(-1,+0) [HALT]
  (1,2)→(13,11) sp=1 f=(-1,+0) [HALT]
  (1,3)→(13,12) sp=1 f=(-1,+0) [HALT]
  (2,0)→(13,9) sp=1 f=(-1,+0)
  (2,1)→(13,10) sp=1 f=(-1,+0)
  (2,2)→(13,11) sp=1 f=(-1,+0)
  (2,3)→(13,12) sp=1 f=(-1,+0)
  (3,0)→(14,9) sp=1 f=(-1,+0)
  (3,1)→(14,10) sp=1 f=(-1,+0)
  (3,2)→(14,11) sp=1 f=(-1,+0)
  (3,3)→(14,12) sp=1 f=(-1,+0)
  (4,0)→(15,9) sp=1 f=(-1,+0)
  (4,1)→(15,10) sp=1 f=(-1,+0)
  (4,2)→(15,11) sp=1 f=(-1,+0)
  (4,3)→(15,12) sp=1 f=(-1,+0)
  (5,0)→(16,9) sp=1 f=(-1,+0)
  (5,1)→(16,10) sp=1 f=(-1,+0)
  (5,2)→(16,11) sp=1 f=(-1,+0)
  (5,3)→(16,12) sp=1 f=(-1,+0)
  (6,4)→(21,13) sp=0 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,8) sp=2 f=(+2,+0) [HALT]
  (0,1)→(12,9) sp=2 f=(+2,+0) [HALT]
  (0,2)→(12,10) sp=2 f=(+2,+0) [HALT]
  (0,4)→(12,12) sp=2 f=(+2,+0) [HALT]
  (0,5)→(12,13) sp=2 f=(+2,+0) [HALT]
  (0,6)→(14,14) sp=2 f=(+2,+0)
  (1,0)→(11,8) sp=2 f=(+2,+0) [HALT]
  (1,1)→(11,9) sp=2 f=(+2,+0) [HALT]
  (1,2)→(11,10) sp=2 f=(+2,+0) [HALT]
  (1,4)→(11,12) sp=2 f=(+2,+0) [HALT]
  (1,5)→(11,13) sp=2 f=(+2,+0) [HALT]
  (1,6)→(15,14) sp=2 f=(+2,+0)
  (2,0)→(10,8) sp=2 f=(+2,+0) [HALT]
  (2,1)→(10,9) sp=2 f=(+2,+0) [HALT]
  (2,2)→(10,10) sp=2 f=(+2,+0) [HALT]
  (2,4)→(10,12) sp=2 f=(+2,+0) [HALT]
  (2,5)→(10,13) sp=2 f=(+2,+0) [HALT]
  (2,6)→(14,14) sp=2 f=(+2,+0)
  (3,0)→(5,8) sp=0 f=(+1,+0)
  (3,1)→(5,9) sp=0 f=(+1,+0)
  (3,2)→(5,10) sp=0 f=(+1,+0)
  (3,3)→(5,11) sp=0 f=(+1,+0)
  (3,4)→(5,12) sp=0 f=(+1,+0)
  (3,5)→(5,13) sp=0 f=(+1,+0)
  (3,6)→(5,14) sp=0 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 4), (2, 5)], cols=[8, 9, 10, 11, 12]

### Target assignment
- A targets: RefusedFlank, centroid=(9.72, 11.0)
- B targets: Horseshoe, centroid=(13.96, 10.6)

### Advance phase
- A cells moved: 16
  - orig (2, 0): (13, 9) → (12, 9)
  - orig (2, 1): (13, 10) → (12, 10)
  - orig (2, 2): (13, 11) → (12, 11)
  - orig (2, 3): (13, 12) → (12, 12)
  - orig (3, 0): (14, 9) → (13, 9)
  - orig (3, 1): (14, 10) → (13, 10)
  - orig (3, 2): (14, 11) → (13, 11)
  - orig (3, 3): (14, 12) → (13, 12)
  ... +8 more
- B cells moved: 3
  - orig (0, 6): (14, 14) → (12, 14)
  - orig (1, 6): (15, 14) → (13, 14)
  - orig (2, 6): (14, 14) → (12, 14)

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[8, 9, 10, 11, 12]
    A contact cells (12): [(11, 9), (11, 10), (11, 11), (11, 12), (12, 9), (12, 10), (12, 11), (12, 12), (13, 9), (13, 10)]...
    B contact cells (15): [(10, 8), (10, 9), (10, 10), (10, 12), (10, 13), (11, 8), (11, 9), (11, 10), (11, 12), (11, 13)]...

### Engagement pool components
  - pair 0: primary_col=10
    A: role=engaged off=0 base_pool=6 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.50
    B: role=flank_engaged off=0 base_pool=7 troops_frac=1.00 engage_frac=1.00 momentum_speed=2.00

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
r 5  .  .  .  B  B  B  B  B  B  B  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  B  B  B  .  B  B  .  .  .  . 
r11  .  .  .  B  #  #  A  #  B  .  .  .  . 
r12  .  .  .  B  #  #  A  #  B  B  .  .  . 
r13  .  .  .  .  A  A  A  A  .  B  .  .  . 
r14  .  .  .  .  A  A  A  A  .  .  .  .  . 
r15  .  .  .  .  A  A  A  A  .  .  .  .  . 
r16  .  .  .  .  .  .  .  .  .  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  A  .  .  .  . 
```

---

## Tick 6 — Phase 1, Tick-in-phase 6

### State at tick start
- A: hp=9/20, sz=1/4, morale=5/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=16/20, sz=3/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(11,9) sp=2 f=(-2,+0) [HALT]
  (0,1)→(11,10) sp=2 f=(-2,+0) [HALT]
  (0,2)→(11,11) sp=2 f=(-2,+0) [HALT]
  (0,3)→(11,12) sp=2 f=(-2,+0) [HALT]
  (1,0)→(13,9) sp=1 f=(-1,+0) [HALT]
  (1,1)→(13,10) sp=1 f=(-1,+0) [HALT]
  (1,2)→(13,11) sp=1 f=(-1,+0) [HALT]
  (1,3)→(13,12) sp=1 f=(-1,+0) [HALT]
  (2,0)→(12,9) sp=1 f=(-1,+0)
  (2,1)→(12,10) sp=1 f=(-1,+0)
  (2,2)→(12,11) sp=1 f=(-1,+0)
  (2,3)→(12,12) sp=1 f=(-1,+0)
  (3,0)→(13,9) sp=1 f=(-1,+0)
  (3,1)→(13,10) sp=1 f=(-1,+0)
  (3,2)→(13,11) sp=1 f=(-1,+0)
  (3,3)→(13,12) sp=1 f=(-1,+0)
  (4,0)→(14,9) sp=1 f=(-1,+0)
  (4,1)→(14,10) sp=1 f=(-1,+0)
  (4,2)→(14,11) sp=1 f=(-1,+0)
  (4,3)→(14,12) sp=1 f=(-1,+0)
  (5,0)→(15,9) sp=1 f=(-1,+0)
  (5,1)→(15,10) sp=1 f=(-1,+0)
  (5,2)→(15,11) sp=1 f=(-1,+0)
  (5,3)→(15,12) sp=1 f=(-1,+0)
  (6,4)→(21,13) sp=0 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,8) sp=2 f=(+2,+0) [HALT]
  (0,1)→(12,9) sp=2 f=(+2,+0) [HALT]
  (0,2)→(12,10) sp=2 f=(+2,+0) [HALT]
  (0,4)→(12,12) sp=2 f=(+2,+0) [HALT]
  (0,5)→(12,13) sp=2 f=(+2,+0) [HALT]
  (0,6)→(12,14) sp=2 f=(-2,+0)
  (1,0)→(11,8) sp=2 f=(+2,+0) [HALT]
  (1,1)→(11,9) sp=2 f=(+2,+0) [HALT]
  (1,2)→(11,10) sp=2 f=(+2,+0) [HALT]
  (1,4)→(11,12) sp=2 f=(+2,+0) [HALT]
  (1,5)→(11,13) sp=2 f=(+2,+0) [HALT]
  (1,6)→(13,14) sp=2 f=(-2,+0)
  (2,0)→(10,8) sp=2 f=(+2,+0) [HALT]
  (2,1)→(10,9) sp=2 f=(+2,+0) [HALT]
  (2,2)→(10,10) sp=2 f=(+2,+0) [HALT]
  (2,4)→(10,12) sp=2 f=(+2,+0) [HALT]
  (2,5)→(10,13) sp=2 f=(+2,+0) [HALT]
  (2,6)→(12,14) sp=2 f=(-2,+0)
  (3,0)→(5,8) sp=0 f=(+1,+0)
  (3,1)→(5,9) sp=0 f=(+1,+0)
  (3,2)→(5,10) sp=0 f=(+1,+0)
  (3,3)→(5,11) sp=0 f=(+1,+0)
  (3,4)→(5,12) sp=0 f=(+1,+0)
  (3,5)→(5,13) sp=0 f=(+1,+0)
  (3,6)→(5,14) sp=0 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 4), (2, 5)], cols=[8, 9, 10, 11, 12]

### Target assignment
- A targets: RefusedFlank, centroid=(9.48, 11.0)
- B targets: Horseshoe, centroid=(13.32, 10.6)

### Advance phase
- A cells moved: 12
  - orig (3, 0): (13, 9) → (12, 9)
  - orig (3, 1): (13, 10) → (12, 10)
  - orig (3, 2): (13, 11) → (12, 11)
  - orig (3, 3): (13, 12) → (12, 12)
  - orig (4, 0): (14, 9) → (13, 9)
  - orig (4, 1): (14, 10) → (13, 10)
  - orig (4, 2): (14, 11) → (13, 11)
  - orig (4, 3): (14, 12) → (13, 12)
  ... +4 more
- B cells moved: 2
  - orig (0, 6): (12, 14) → (14, 14)
  - orig (2, 6): (12, 14) → (14, 14)

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[8, 9, 10, 11, 12]
    A contact cells (12): [(11, 9), (11, 10), (11, 11), (11, 12), (12, 9), (12, 10), (12, 11), (12, 12), (13, 9), (13, 10)]...
    B contact cells (15): [(10, 8), (10, 9), (10, 10), (10, 12), (10, 13), (11, 8), (11, 9), (11, 10), (11, 12), (11, 13)]...

### Engagement pool components
  - pair 0: primary_col=10
    A: role=engaged off=0 base_pool=5 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.50
    B: role=flank_engaged off=0 base_pool=7 troops_frac=1.00 engage_frac=1.00 momentum_speed=2.00

### Engagement result
- A dmg taken: 3
- B dmg taken: 0
- engagements: 1

### End-of-tick deltas
- A: hp 9→6 (Δ-3), sz 1→1 (Δ0), morale 5→4 (Δ-1)
- B: hp 16→16 (Δ0), sz 3→3 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  B  B  B  B  B  B  B  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  B  B  B  .  B  B  .  .  .  . 
r11  .  .  .  B  #  #  A  #  B  .  .  .  . 
r12  .  .  .  B  #  #  A  #  B  .  .  .  . 
r13  .  .  .  .  A  A  A  A  .  B  .  .  . 
r14  .  .  .  .  A  A  A  A  .  B  .  .  . 
r15  .  .  .  .  .  .  .  .  .  .  .  .  . 
r16  .  .  .  .  .  .  .  .  .  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  A  .  .  .  . 
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
- A: hp=6/20, sz=1/4, morale=4/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False
- B: hp=16/20, sz=3/4, morale=6/6, disc=5, cmd=4, h/sz=5, stance=balanced, broken=False, routed=False

### A cells (pre-movement)
```
  (0,0)→(11,9) sp=2 f=(-2,+0) [HALT]
  (0,1)→(11,10) sp=2 f=(-2,+0) [HALT]
  (0,2)→(11,11) sp=2 f=(-2,+0) [HALT]
  (0,3)→(11,12) sp=2 f=(-2,+0) [HALT]
  (1,0)→(13,9) sp=1 f=(-1,+0) [HALT]
  (1,1)→(13,10) sp=1 f=(-1,+0) [HALT]
  (1,2)→(13,11) sp=1 f=(-1,+0) [HALT]
  (1,3)→(13,12) sp=1 f=(-1,+0) [HALT]
  (2,0)→(12,9) sp=1 f=(-1,+0) [HALT]
  (2,1)→(12,10) sp=1 f=(-1,+0) [HALT]
  (2,2)→(12,11) sp=1 f=(-1,+0) [HALT]
  (2,3)→(12,12) sp=1 f=(-1,+0) [HALT]
  (3,0)→(12,9) sp=1 f=(-1,+0)
  (3,1)→(12,10) sp=1 f=(-1,+0)
  (3,2)→(12,11) sp=1 f=(-1,+0)
  (3,3)→(12,12) sp=1 f=(-1,+0)
  (4,0)→(13,9) sp=1 f=(-1,+0)
  (4,1)→(13,10) sp=1 f=(-1,+0)
  (4,2)→(13,11) sp=1 f=(-1,+0)
  (4,3)→(13,12) sp=1 f=(-1,+0)
  (5,0)→(14,9) sp=1 f=(-1,+0)
  (5,1)→(14,10) sp=1 f=(-1,+0)
  (5,2)→(14,11) sp=1 f=(-1,+0)
  (5,3)→(14,12) sp=1 f=(-1,+0)
  (6,4)→(21,13) sp=0 f=(-1,+0)
```

### B cells (pre-movement)
```
  (0,0)→(12,8) sp=2 f=(+2,+0) [HALT]
  (0,1)→(12,9) sp=2 f=(+2,+0) [HALT]
  (0,2)→(12,10) sp=2 f=(+2,+0) [HALT]
  (0,4)→(12,12) sp=2 f=(+2,+0) [HALT]
  (0,5)→(12,13) sp=2 f=(+2,+0) [HALT]
  (0,6)→(14,14) sp=2 f=(+2,+0)
  (1,0)→(11,8) sp=2 f=(+2,+0) [HALT]
  (1,1)→(11,9) sp=2 f=(+2,+0) [HALT]
  (1,2)→(11,10) sp=2 f=(+2,+0) [HALT]
  (1,4)→(11,12) sp=2 f=(+2,+0) [HALT]
  (1,5)→(11,13) sp=2 f=(+2,+0) [HALT]
  (1,6)→(13,14) sp=2 f=(-2,+0)
  (2,0)→(10,8) sp=2 f=(+2,+0) [HALT]
  (2,1)→(10,9) sp=2 f=(+2,+0) [HALT]
  (2,2)→(10,10) sp=2 f=(+2,+0) [HALT]
  (2,4)→(10,12) sp=2 f=(+2,+0) [HALT]
  (2,5)→(10,13) sp=2 f=(+2,+0) [HALT]
  (2,6)→(14,14) sp=2 f=(+2,+0)
  (3,0)→(5,8) sp=0 f=(+1,+0)
  (3,1)→(5,9) sp=0 f=(+1,+0)
  (3,2)→(5,10) sp=0 f=(+1,+0)
  (3,3)→(5,11) sp=0 f=(+1,+0)
  (3,4)→(5,12) sp=0 f=(+1,+0)
  (3,5)→(5,13) sp=0 f=(+1,+0)
  (3,6)→(5,14) sp=0 f=(+1,+0)
```

### Pre-movement contacts (halt source)
- 1 contact pair(s)
  - pair 0: A halted cells=[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)], B halted cells=[(0, 0), (0, 1), (0, 2), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 4), (2, 5)], cols=[8, 9, 10, 11, 12]

### Target assignment
- A targets: RefusedFlank, centroid=(9.64, 11.0)
- B targets: Horseshoe, centroid=(12.84, 10.6)

### Advance phase
- A cells moved: 12
  - orig (3, 0): (12, 9) → (11, 9)
  - orig (3, 1): (12, 10) → (11, 10)
  - orig (3, 2): (12, 11) → (11, 11)
  - orig (3, 3): (12, 12) → (11, 12)
  - orig (4, 0): (13, 9) → (12, 9)
  - orig (4, 1): (13, 10) → (12, 10)
  - orig (4, 2): (13, 11) → (12, 11)
  - orig (4, 3): (13, 12) → (12, 12)
  ... +4 more
- B cells moved: 3
  - orig (0, 6): (14, 14) → (12, 14)
  - orig (1, 6): (13, 14) → (11, 14)
  - orig (2, 6): (14, 14) → (12, 14)

### Cross-side contention
- 0 cells resolved

### Post-movement contact pairs
- 1 contact pair(s)
  - pair 0: cols=[8, 9, 10, 11, 12]
    A contact cells (12): [(11, 9), (11, 10), (11, 11), (11, 12), (12, 9), (12, 10), (12, 11), (12, 12), (13, 9), (13, 10)]...
    B contact cells (15): [(10, 8), (10, 9), (10, 10), (10, 12), (10, 13), (11, 8), (11, 9), (11, 10), (11, 12), (11, 13)]...

### Engagement pool components
  - pair 0: primary_col=10
    A: role=engaged off=0 base_pool=5 troops_frac=1.00 engage_frac=1.00 momentum_speed=1.50
    B: role=flank_engaged off=0 base_pool=7 troops_frac=1.00 engage_frac=1.00 momentum_speed=2.00

### Engagement result
- A dmg taken: 4
- B dmg taken: 0
- engagements: 1

### End-of-tick deltas
- A: hp 6→2 (Δ-4), sz 1→0 (Δ-1), morale 4→4 (Δ0)
- B: hp 16→16 (Δ0), sz 3→3 (Δ0), morale 6→6 (Δ0)

### Grid at end of tick
```
     5  6  7  8  9 10 11 12 13 14 15 16 17
r 3  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 4  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 5  .  .  .  B  B  B  B  B  B  B  .  .  . 
r 6  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 7  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 8  .  .  .  .  .  .  .  .  .  .  .  .  . 
r 9  .  .  .  .  .  .  .  .  .  .  .  .  . 
r10  .  .  .  B  B  B  .  B  B  .  .  .  . 
r11  .  .  .  B  #  #  A  #  B  B  .  .  . 
r12  .  .  .  B  #  #  A  #  B  B  .  .  . 
r13  .  .  .  .  A  A  A  A  .  .  .  .  . 
r14  .  .  .  .  .  .  .  .  .  .  .  .  . 
r15  .  .  .  .  .  .  .  .  .  .  .  .  . 
r16  .  .  .  .  .  .  .  .  .  .  .  .  . 
r17  .  .  .  .  .  .  .  .  .  .  .  .  . 
r18  .  .  .  .  .  .  .  .  .  .  .  .  . 
r19  .  .  .  .  .  .  .  .  .  .  .  .  . 
r20  .  .  .  .  .  .  .  .  .  .  .  .  . 
r21  .  .  .  .  .  .  .  .  A  .  .  .  . 
```

---

## Tick 8 — Phase 2, Tick-in-phase 2

**Battle ended:** A.routed=True, B.routed=False
---

## Battle result

- Winner: **B**
- Turns: 8
- Phases completed: 1
- Final A: hp=2/20, sz=0/4, routed=True
- Final B: hp=16/20, sz=3/4, routed=False
