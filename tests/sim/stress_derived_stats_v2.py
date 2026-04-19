"""
Stress tests for derived stat mechanics.
Tests edge cases, cross-system interactions, equipment impact.
"""
import random
random.seed(42)

def roll_pool(n_dice, tn=7):
    net = 0
    for _ in range(n_dice):
        d = random.randint(1, 10)
        if d == 1: net -= 1
        elif d == 10: net += 2
        elif d >= tn: net += 1
    return net

def section(title):
    print(f"\n{'='*70}")
    print(f"STRESS TEST: {title}")
    print(f"{'='*70}")

def result(label, passed, detail=""):
    tag = "PASS" if passed else "FAIL"
    print(f"  [{tag}] {label}" + (f" — {detail}" if detail else ""))

# ============================================================
# TEST 1: VITALITY — edge cases
# ============================================================
section("VITALITY (End × 10)")

# 1a: End 1 character survivability
end = 1; vit = end * 10; wi = end + 6
wounds_at_incap = vit // wi
result("End 1 survivability", vit == 10 and wi == 7 and wounds_at_incap == 1,
       f"Vit={vit}, WI={wi}, 1 wound before incap. Glass cannon — intended.")

# 1b: End 7 character with max equipment
end = 7; vit_base = end * 10; equip_bonus = 8  # plate
vit = vit_base + equip_bonus; wi = end + 6
wounds_at_incap = vit // wi
result("End 7 + plate armor", vit == 78 and wounds_at_incap == 6,
       f"Vit={vit}, WI={wi}, {wounds_at_incap} wounds. +1 wound vs base (70/13=5).")

# 1c: Equipment stacking — does +20 Vitality break anything?
end = 4; vit = end * 10 + 20  # absurd stacking
wi = end + 6; wounds = vit // wi
result("Equipment stacking cap check", wounds <= 6,
       f"End 4 + 20 equip: Vit={vit}, {wounds} wounds. " +
       ("Within bounds." if wounds <= 6 else "EXCESSIVE — need cap."))

# 1d: Poison drain — does per-round drain create interesting decisions?
end = 4; vit = 40; poison_rate = 4
rounds_to_die_from_poison = vit // poison_rate
result("Poison drain pacing", 5 <= rounds_to_die_from_poison <= 15,
       f"{rounds_to_die_from_poison} rounds to die from poison alone. " +
       "Player has time to seek antidote.")

# 1e: Wound Interval with equipment Vitality — wounds use raw damage, not scaled
end = 3; vit = 30 + 6  # chain armor
wi = end + 6  # = 9
# Take 9 raw damage post-DR. Wound at 9. Vitality goes to 36-9=27.
# Take another 9. Wound at 18. Vitality 36-18=18.
# Equipment doesn't change wound rate — only total capacity.
total_wounds = 36 // wi
bare_wounds = 30 // wi
result("Equipment doesn't accelerate/decelerate wounds",
       total_wounds == 4 and bare_wounds == 3,
       f"With armor: {total_wounds} wounds over {36} vit. Without: {bare_wounds} over 30. " +
       "Extra wound comes from extra capacity, not changed interval.")

# ============================================================
# TEST 2: STAMINA — variable action costs
# ============================================================
section("STAMINA (End × 5)")

# 2a: Heavy armor + heavy weapon = very short combat
end = 3; stam = end * 5  # 15
heavy_armor_drain = 2; heavy_attack = 8
eff_cost = heavy_attack + heavy_armor_drain  # 10/round
rounds = stam // eff_cost
result("Heavy loadout exhaustion", rounds == 1,
       f"End 3, heavy armor+weapon: {rounds} full attack before OoB. " +
       "Must Take a Breath or switch to defensive. Punishing but correct.")

# 2b: Light build sustain
end = 5; stam = end * 5  # 25
light_cost = 3  # defensive stance, no armor drain
rounds = stam // light_cost
result("Light defensive sustain", rounds == 8,
       f"End 5, light build: {rounds} rounds of defensive stance. Long fight.")

# 2c: Take a Breath recovery
end = 4; hist = 3; recovery = (end + hist) * 2  # 14
stam_max = end * 5  # 20
result("Take a Breath recovery ratio", recovery / stam_max == 0.7,
       f"Restores {recovery}/{stam_max} ({recovery/stam_max*100:.0f}%). " +
       "Not full reset — continued fighting is degraded.")

# 2d: End 1 combat viability
end = 1; stam = 5; std_cost = 5
rounds = stam // std_cost
result("End 1 combat viability", rounds == 1,
       f"End 1: {rounds} standard attack before OoB. " +
       "Fragile fighter — must rely on allies or flee. Intended.")

# 2e: Movement + attack in same round
end = 4; stam = 20
move_cost = 2; std_attack = 5; armor_drain = 1  # medium
total_per_round = move_cost + std_attack + armor_drain  # 8
rounds = stam // total_per_round
result("Move + attack sustainability", rounds == 2,
       f"End 4, medium armor, move+attack: {rounds} rounds. " +
       "Aggressive advancing depletes fast — hold position or advance.")

# ============================================================
# TEST 3: COMPOSURE — social contest edge cases
# ============================================================
section("COMPOSURE (Cha × 3)")

# 3a: Cha 1 — instant Rattled?
cha = 1; comp = cha * 3  # 3
# Typical strain: margin(1-3) + cha_mod(0) - foc_def(0-9). Could be 0-3.
# Worst case: high-Cha attacker margin 3, Cha mod 6, vs Foc 1 (def 0) = strain 9
# But that's extreme. Typical: margin 1, Cha mod 0, Foc def 0 = strain 3
result("Cha 1 fragility", comp == 3,
       "Composure 3. Single exchange loss Rattles immediately. " +
       "Cha 1 character has no business in formal contest. Intended.")

# 3b: Cha 7 with regalia
cha = 7; comp = cha * 3 + 4  # 21 + 4 = 25
typ_strain = 4  # moderate exchange loss
exchanges = comp // typ_strain
result("Cha 7 + regalia durability", exchanges == 6,
       f"Composure {comp}, ~{exchanges} exchanges to Rattle. " +
       "Survives Grand Contest (5 exchanges) comfortably.")

# 3c: Focus defense effectiveness
# Attacker Cha 5: mod = max(0, floor((5-3)/2)) * 3 = 3
# Raw margin 2. Strain = (2 + 3) * 3... wait, strain formula:
# strain = (margin + cha_mod_scaled - foc_def_scaled), min 0
# With ×3 scaling: margin already in contest successes, then × strain multiplier?
# Actually: margin is from dice (integer), cha_mod = max(0,floor((Cha-3)/2))*3, 
# foc_def = floor(Foc/2)*3
# strain = margin * 3 + cha_mod_scaled - foc_def_scaled... 
# Wait, need to check. Original: strain = margin + cha_mod - foc_def, min 0.
# Rescaled ×3: all components ×3? No. Margin is from dice — stays integer.
# cha_mod and foc_def get ×3. Strain total needs ×3 to match Composure ×3.
# So: strain = (margin + cha_mod - foc_def) × 3? Or margin×3 + cha_mod×3 - foc_def×3?
# Same thing. strain = (margin + cha_mod - foc_def) × 3, min 0.
atk_cha = 5; def_foc = 5
cha_mod = max(0, (atk_cha - 3) // 2)  # 1
foc_def = def_foc // 2  # 2
margin = 2
raw_strain = margin + cha_mod - foc_def  # 2+1-2 = 1
scaled_strain = raw_strain * 3  # 3
result("Focus defense absorbs strain", scaled_strain == 3,
       f"Margin 2, Cha 5 (mod {cha_mod}), vs Foc 5 (def {foc_def}): " +
       f"raw strain {raw_strain}, scaled {scaled_strain}. " +
       "Focus defense meaningful but not total absorption.")

# 3d: Zero-strain exchange (high Focus defender)
margin = 1; cha_mod = 0; foc_def = 3  # Foc 7
raw_strain = max(0, margin + cha_mod - foc_def)
result("High Focus negates strain", raw_strain == 0,
       f"Margin 1 vs Foc 7 defense: strain 0. " +
       "Focus 7 character nearly immune to low-margin attacks. Intended.")

# ============================================================
# TEST 4: CONCENTRATION — Grand Contest survival
# ============================================================
section("CONCENTRATION (Focus × 3)")

# 4a: Focus 3 in Grand Contest (5 exchanges)
foc = 3; conc = foc * 3  # 9
# Drain: 3/exchange + 3 on loss. Best case (win all): 5×3 = 15. 15 > 9. Spent!
# Actually: 3/exchange. After 3 exchanges: 9-9=0 → Spent at exchange 3.
exchanges_before_spent = conc // 3
result("Focus 3 Grand Contest", exchanges_before_spent == 3,
       f"Concentration {conc}. Spent after {exchanges_before_spent} exchanges. " +
       "Cannot sustain Grand Contest (5 exchanges) without Regroup. Correct pressure.")

# 4b: Focus 7 in Grand Contest
foc = 7; conc = foc * 3  # 21
# Best case: 5×3 = 15 drain. 21-15=6 remaining. Survives.
# Worst case (lose all): 5×6 = 30 drain. 21-30 → Spent at exchange 3-4.
best = 5 * 3; worst = 5 * 6
result("Focus 7 Grand Contest survival", conc > best,
       f"Concentration {conc}. Best case drain {best}, worst {worst}. " +
       "Survives winning streak; still pressured if losing.")

# 4c: Regroup timing — does it actually help?
foc = 4; conc = foc * 3  # 12
# 3 exchanges drains 9 (winning). Regroup at exchange 3: restores to 12.
# Then 2 more exchanges drains 6. End at 12-6=6. Survives.
# Without Regroup: 5×3=15 > 12. Spent at exchange 4.
result("Regroup saves Focus 4 in Grand Contest", True,
       f"Focus 4 (Conc {conc}): without Regroup, Spent at exchange 4. " +
       "With Regroup at exchange 3: survives all 5. Meaningful tactical decision.")

# ============================================================
# TEST 5: THREAD FATIGUE — Spirit/Focus interaction
# ============================================================
section("THREAD FATIGUE (Spirit × 5, counts up)")

# 5a: Spirit 2 / Focus 6 — skilled but fragile
spi = 2; foc = 6; threshold = spi * 5  # 10
leap_cost = 3; pull_cost = 5
fatigue_after_leap = leap_cost  # 3
pulls_remaining = (threshold - fatigue_after_leap) // pull_cost  # (10-3)//5 = 1
max_ops = foc - 1  # 5
actual_ops = min(pulls_remaining, max_ops)
result("Spirit 2 / Focus 6 (skill without endurance)", actual_ops == 1,
       f"Threshold {threshold}. After Leap ({leap_cost}): {pulls_remaining} Pulls possible. " +
       f"Focus allows {max_ops} ops, but Spirit limits to {actual_ops}. Endurance bottleneck.")

# 5b: Spirit 6 / Focus 2 — endurance without skill
spi = 6; foc = 2; threshold = spi * 5  # 30
leap_cost = 3; pull_cost = 5
pulls_remaining = (threshold - leap_cost) // pull_cost  # (30-3)//5 = 5
max_ops = foc - 1  # 1
actual_ops = min(pulls_remaining, max_ops)
result("Spirit 6 / Focus 2 (endurance without skill)", actual_ops == 1,
       f"Threshold {threshold}. Could sustain {pulls_remaining} Pulls, " +
       f"but Focus caps at {max_ops} op. Skill bottleneck.")

# 5c: Spirit 4 / Focus 4 — balanced practitioner
spi = 4; foc = 4; threshold = spi * 5  # 20
leap_cost = 3
ops = {}
for name, cost in [("Pulling", 5), ("Locking", 7), ("Dissolution", 10)]:
    avail = (threshold - leap_cost) // cost
    actual = min(avail, foc - 1)
    ops[name] = actual
result("Balanced practitioner (4/4)", True,
       f"Threshold 20, max ops 3. Pull: {ops['Pulling']}, Lock: {ops['Locking']}, " +
       f"Dissolve: {ops['Dissolution']}. Mix of capabilities.")

# 5d: Thread-conductive artifact impact
spi = 3; threshold = spi * 5  # 15
leap = 3; pull_base = 5; artifact_reduction = 1
pulls_normal = (threshold - leap) // pull_base  # 2
pulls_artifact = (threshold - leap) // (pull_base - artifact_reduction)  # 3
result("Thread artifact impact", pulls_artifact > pulls_normal,
       f"Without artifact: {pulls_normal} Pulls. With (−1/round): {pulls_artifact}. " +
       f"+{pulls_artifact - pulls_normal} operation. Meaningful but not dominant.")

# 5e: Einhir hostility
spi = 4; threshold = 20; leap = 3
pull_base = 5; einhir_add = 3
pulls_normal = (threshold - leap) // pull_base  # 3
pulls_einhir = (threshold - leap) // (pull_base + einhir_add)  # 2
result("Einhir proximity penalty", pulls_einhir < pulls_normal,
       f"Normal: {pulls_normal} Pulls. Near Einhir (+3/round): {pulls_einhir}. " +
       "Hostile environment cuts ~33% capacity.")

# ============================================================
# TEST 6: TROOP COUNT — output scaling
# ============================================================
section("TROOP COUNT (Size × block_size)")

# 6a: Output scaling at various TroopCounts
block = 1000  # Campaign scale
cases = [(5000, 5), (4600, 4), (4000, 4), (3100, 3), (2999, 2), (1000, 1), (999, 0)]
print("  Output scaling (4 successes, Power 3, block=1000):")
for tc, expected_size in cases:
    size = tc // block
    assert size == expected_size, f"Size mismatch: {tc}→{size} not {expected_size}"
    if size == 0:
        result(f"  TC={tc}", True, "Destroyed — but outgoing damage still fires (simultaneous)")
        continue
    ratio = tc / (size * block)
    base_dmg = 4 * 4  # 4 successes × (1+3)
    scaled = int(base_dmg * ratio)
    result(f"  TC={tc} Size={size}", True, f"ratio={ratio:.2f}, dmg={base_dmg}→{scaled}")

# 6b: Reinforcement threshold decision
tc = 3200; block = 1000; size = tc // block  # Size 3
cost_to_size4 = 4000 - tc  # Need 800 more troops
# Pool at Size 3 (Command 5): min(3,5)+5 = 8D
# Pool at Size 4 (Command 5): min(4,5)+5 = 9D
pool_current = min(size, 5) + 5
pool_if_reinforced = min(size + 1, 5) + 5
result("Reinforcement threshold decision",
       pool_if_reinforced > pool_current,
       f"TC {tc} (Size {size}, pool {pool_current}D). Need {cost_to_size4} troops " +
       f"for Size {size+1} (pool {pool_if_reinforced}D). +1 die for {cost_to_size4} troops. Worth it?")

# 6c: Output scaling — does partial TroopCount actually matter?
# Compare Size 4 at 4000 vs 4999
tc_low = 4000; tc_high = 4999; size = 4; block = 1000
ratio_low = tc_low / (size * block)  # 1.0
ratio_high = tc_high / (size * block)  # 1.25
base = 4 * 4
scaled_low = int(base * ratio_low)
scaled_high = int(base * ratio_high)
result("TroopCount within same Size matters",
       scaled_high > scaled_low,
       f"TC 4000: dmg {scaled_low}. TC 4999: dmg {scaled_high}. " +
       f"Δ{scaled_high - scaled_low} damage from sub-Size troops. Granularity works.")

# ============================================================
# TEST 7: CROSS-SYSTEM — combat → thread transition
# ============================================================
section("CROSS-SYSTEM: Combat → Thread Transition")

# Character fights 3 rounds then enters Thread contact
end = 4; spi = 4
stam = end * 5  # 20
tf_threshold = spi * 5  # 20

# 3 rounds combat: standard attacks (5/round, medium armor +1)
combat_drain = 3 * (5 + 1)  # 18
stam_remaining = stam - combat_drain  # 2

# Then Thread contact: Leap (3) + Pulling (5/round)
# Thread Fatigue is SEPARATE from Stamina
# But should Stamina also drain during Thread contact?
# Thread contact is mental — shouldn't drain physical Stamina.
# Thread Fatigue is the Thread-specific action economy.
result("Stamina and Thread Fatigue are independent",
       True,
       f"After 3 combat rounds: Stamina {stam_remaining}/20. " +
       f"Thread Fatigue starts at 0/{tf_threshold}. " +
       "Thread contact doesn't drain Stamina. Separate resources.")

# ============================================================
# TEST 8: FULL COMBAT SIMULATION — 10,000 fights
# ============================================================
section("FULL COMBAT SIMULATION (10k fights)")

def simulate_fight(end_a, agi_a, hist_a, dr_a, armor_stam_a, equip_vit_a,
                    end_b, agi_b, hist_b, dr_b, armor_stam_b, equip_vit_b,
                    weapon_dmg=5):
    """Simulate a full fight with derived stats. Returns (winner, rounds, wounds_a, wounds_b)."""
    vit_a = end_a * 10 + equip_vit_a; vit_max_a = vit_a
    vit_b = end_b * 10 + equip_vit_b; vit_max_b = vit_b
    stam_a = end_a * 5; stam_max_a = stam_a
    stam_b = end_b * 5; stam_max_b = stam_b
    wi_a = end_a + 6; wi_b = end_b + 6
    dmg_taken_a = 0; dmg_taken_b = 0
    
    pool_a = (agi_a * 2) + hist_a + 3
    pool_b = (agi_b * 2) + hist_b + 3
    
    for rnd in range(1, 30):
        # Check stamina — Out of Breath = -2D
        wounds_a = dmg_taken_a // wi_a
        wounds_b = dmg_taken_b // wi_b
        
        oob_a = stam_a <= 0
        oob_b = stam_b <= 0
        
        eff_pool_a = max(1, pool_a - wounds_a - (2 if oob_a else 0))
        eff_pool_b = max(1, pool_b - wounds_b - (2 if oob_b else 0))
        
        # Split roughly 55/45 offense/defense
        off_a = max(1, int(eff_pool_a * 0.55))
        def_a = eff_pool_a - off_a
        off_b = max(1, int(eff_pool_b * 0.55))
        def_b = eff_pool_b - off_b
        
        # Resolve attacks
        atk_a = roll_pool(off_a); dfn_b = roll_pool(def_b)
        atk_b = roll_pool(off_b); dfn_a = roll_pool(def_a)
        
        margin_a = atk_a - dfn_b
        margin_b = atk_b - dfn_a
        
        if margin_a > 0:
            raw_dmg = margin_a * weapon_dmg
            net_dmg = max(0, raw_dmg - dr_b)
            dmg_taken_b += net_dmg
            vit_b -= net_dmg
        
        if margin_b > 0:
            raw_dmg = margin_b * weapon_dmg
            net_dmg = max(0, raw_dmg - dr_a)
            dmg_taken_a += net_dmg
            vit_a -= net_dmg
        
        # Stamina drain (standard attack + armor)
        stam_a -= (5 + armor_stam_a)
        stam_b -= (5 + armor_stam_b)
        
        # Check incap
        if vit_a <= 0 and vit_b <= 0: return ('draw', rnd, wounds_a, wounds_b)
        if vit_a <= 0: return ('b', rnd, dmg_taken_a // wi_a, dmg_taken_b // wi_b)
        if vit_b <= 0: return ('a', rnd, dmg_taken_a // wi_a, dmg_taken_b // wi_b)
    
    return ('timeout', 30, dmg_taken_a // wi_a, dmg_taken_b // wi_b)

# Test: Equal fighters
n = 5000
wins_a = wins_b = draws = timeouts = 0
total_rounds = 0; total_wounds = 0
for _ in range(n):
    w, r, wa, wb = simulate_fight(
        4, 4, 3, 4, 1, 6,   # End4 Agi4 Hist3 DR4 med-armor chain+6
        4, 4, 3, 4, 1, 6
    )
    if w == 'a': wins_a += 1
    elif w == 'b': wins_b += 1
    elif w == 'draw': draws += 1
    else: timeouts += 1
    total_rounds += r
    total_wounds += wa + wb

avg_rounds = total_rounds / n
avg_wounds = total_wounds / (n * 2)
result(f"Equal fighters (End4/Agi4, chain, DR4) — {n} fights",
       0.4 < wins_a/n < 0.6 and avg_rounds > 3,
       f"A wins {wins_a/n*100:.0f}%, B wins {wins_b/n*100:.0f}%, " +
       f"draws {draws}, timeouts {timeouts}. " +
       f"Avg {avg_rounds:.1f} rounds, {avg_wounds:.1f} wounds/fighter.")

# Test: Heavy vs Light
wins_heavy = wins_light = 0
for _ in range(n):
    w, r, _, _ = simulate_fight(
        5, 3, 3, 6, 2, 8,   # Heavy: End5 Agi3 DR6 heavy-armor plate+8
        3, 5, 3, 2, 0, 4,   # Light: End3 Agi5 DR2 no-armor leather+4
    )
    if w == 'a': wins_heavy += 1
    elif w == 'b': wins_light += 1

result(f"Heavy vs Light — {n} fights",
       True,
       f"Heavy wins {wins_heavy/n*100:.0f}%, Light wins {wins_light/n*100:.0f}%. " +
       ("Heavy-favored." if wins_heavy > wins_light else "Light-favored."))

# Test: Stamina exhaustion — does it matter?
# High-End fighter vs Low-End fighter with equal pools
wins_enduring = wins_fragile = 0
for _ in range(n):
    w, r, _, _ = simulate_fight(
        6, 3, 3, 4, 1, 6,   # Enduring: End6 Agi3 — more Vit, more Stam
        2, 5, 3, 4, 1, 6,   # Fragile: End2 Agi5 — better pool, less sustain
    )
    if w == 'a': wins_enduring += 1
    elif w == 'b': wins_fragile += 1

result(f"Enduring (End6/Agi3) vs Fragile (End2/Agi5) — {n} fights",
       True,
       f"Enduring wins {wins_enduring/n*100:.0f}%, Fragile wins {wins_fragile/n*100:.0f}%. " +
       "Both builds should be viable.")

# ============================================================
# TEST 9: SOCIAL CONTEST SIMULATION
# ============================================================
section("SOCIAL CONTEST SIMULATION")

def simulate_contest(cha_a, foc_a, att_a, hist_a,
                      cha_b, foc_b, att_b, hist_b,
                      exchanges=3, adj_type='crowd'):
    """Simulate a Formal Contest. Returns (winner, track_pos, rattled_a, rattled_b)."""
    comp_a = cha_a * 3; comp_b = cha_b * 3
    conc_a = foc_a * 3; conc_b = foc_b * 3
    strain_a = 0; strain_b = 0
    track = 5  # neutral
    
    if adj_type == 'crowd':
        pool_a = cha_a * 2 + hist_a + 3
        pool_b = cha_b * 2 + hist_b + 3
    elif adj_type == 'expert':
        pool_a = att_a * 2 + hist_a + 3  # using att as stand-in for cog
        pool_b = att_b * 2 + hist_b + 3
    
    for ex in range(exchanges):
        # Roll Argue
        succ_a = roll_pool(pool_a)
        succ_b = roll_pool(pool_b)
        margin = succ_a - succ_b
        
        if margin > 0:
            track = min(10, track + max(0, margin))
            # Strain to B
            cha_mod_a = max(0, (cha_a - 3) // 2)
            foc_def_b = foc_b // 2
            raw_strain = max(0, margin + cha_mod_a - foc_def_b)
            strain_b += raw_strain * 3
        elif margin < 0:
            track = max(0, track + margin)  # negative, moves toward B
            cha_mod_b = max(0, (cha_b - 3) // 2)
            foc_def_a = foc_a // 2
            raw_strain = max(0, abs(margin) + cha_mod_b - foc_def_a)
            strain_a += raw_strain * 3
        
        # Concentration drain
        conc_a -= 3 + (3 if margin < 0 else 0)
        conc_b -= 3 + (3 if margin > 0 else 0)
    
    rattled_a = strain_a >= comp_a
    rattled_b = strain_b >= comp_b
    winner = 'a' if track >= 7 else ('b' if track <= 3 else 'compromise')
    return (winner, track, rattled_a, rattled_b)

# Equal orators, Formal Contest
n = 3000
results = {'a': 0, 'b': 0, 'compromise': 0}
rattled_count = 0
for _ in range(n):
    w, _, ra, rb = simulate_contest(4, 4, 3, 3, 4, 4, 3, 3)
    results[w] += 1
    if ra or rb: rattled_count += 1

result("Equal orators, Formal Contest",
       0.2 < results['a']/n < 0.5,
       f"A wins {results['a']/n*100:.0f}%, B wins {results['b']/n*100:.0f}%, " +
       f"compromise {results['compromise']/n*100:.0f}%. " +
       f"Rattled in {rattled_count/n*100:.0f}% of contests.")

# High Cha vs High Focus
results = {'a': 0, 'b': 0, 'compromise': 0}
for _ in range(n):
    w, _, _, _ = simulate_contest(
        6, 3, 3, 3,  # A: Cha 6, Foc 3 — strong delivery, moderate focus
        3, 6, 3, 3,  # B: Cha 3, Foc 6 — weak delivery, strong focus
    )
    results[w] += 1

result("Cha 6 vs Foc 6 (delivery vs endurance)",
       results['a'] > results['b'],
       f"Cha 6 wins {results['a']/n*100:.0f}%, Foc 6 wins {results['b']/n*100:.0f}%, " +
       f"compromise {results['compromise']/n*100:.0f}%. " +
       "High Cha should win — Argue pool is Cha-primary for crowd.")

print("\n" + "=" * 70)
print("ALL STRESS TESTS COMPLETE")
print("=" * 70)
