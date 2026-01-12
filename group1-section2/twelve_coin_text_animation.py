# 12 Coins Problem – Text-based Animation Version

import time
import os

# Hidden truth (for demonstration)
FAKE_COIN = 6
FAKE_TYPE = "light"  # "heavy" or "light"

def weight(coin):
    if coin != FAKE_COIN:
        return 1
    return 2 if FAKE_TYPE == "heavy" else 0

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_balance_beam(left_tilt, right_tilt):
    """Draw a simple balance beam visualization"""
    print("     ╔═══════════════════════╗")
    print("     ║     BALANCE BEAM      ║")
    print("     ╚═══════════════════════╝")
    print("              │")
    print("              │")
    
    # Draw the beam with tilt
    if left_tilt > right_tilt:
        # Left side down
        print("  ╭───────────┴───────────╮")
        print("  │                       │")
        print("  ▼                       │")
    elif right_tilt > left_tilt:
        # Right side down
        print("  ╭───────────┴───────────╮")
        print("  │                       │")
        print("  │                       ▼")
    else:
        # Balanced
        print("  ╭───────────┴───────────╮")
        print("  │                       │")
        print("  │                       │")
    
    print("  ╰───────────────────────╯")

def animate_weighing(label, left_coins, right_coins):
    """Animate a single weighing"""
    print(f"\n🎯 {label}")
    print(f"⚖️  Left side: {left_coins}")
    print(f"⚖️  Right side: {right_coins}")
    
    # Calculate weights
    left_weight = sum(weight(c) for c in left_coins)
    right_weight = sum(weight(c) for c in right_coins)
    
    # Show weighing animation
    print("\n⚖️  Weighing...")
    for i in range(3):
        print("." * (i + 1))
        time.sleep(0.5)
    
    # Determine outcome
    if left_weight > right_weight:
        outcome = "LEFT HEAVIER"
        left_tilt = 1
        right_tilt = 0
    elif right_weight > left_weight:
        outcome = "RIGHT HEAVIER"
        left_tilt = 0
        right_tilt = 1
    else:
        outcome = "BALANCED"
        left_tilt = 0
        right_tilt = 0
    
    # Draw the balance beam
    draw_balance_beam(left_tilt, right_tilt)
    
    print(f"\n📊 RESULT: {outcome}")
    print(f"📏 Left weight: {left_weight}, Right weight: {right_weight}")
    
    return outcome

def solve_twelve_coins_animated():
    """Solve the 12 coins problem with animation"""
    clear_screen()
    print("🪙 12 COINS PROBLEM SOLVER 🪙")
    print("=" * 40)
    print(f"🔍 Finding the fake coin... (Coin {FAKE_COIN} is {FAKE_TYPE})")
    print("=" * 40)
    
    # Step 1: First weighing
    time.sleep(2)
    result1 = animate_weighing("WEIGHING 1", [1,2,3,4], [5,6,7,8])
    
    # Step 2: Second weighing
    time.sleep(2)
    if result1 == "BALANCED":
        result2 = animate_weighing("WEIGHING 2", [9,10], [1,2])
    else:
        result2 = animate_weighing("WEIGHING 2", [1,2,5], [3,6,9])
    
    # Step 3: Third weighing
    time.sleep(2)
    if result1 == "BALANCED" and result2 == "BALANCED":
        result3 = animate_weighing("WEIGHING 3", [11], [1])
    elif result1 == "BALANCED" and result2 != "BALANCED":
        result3 = animate_weighing("WEIGHING 3", [9], [1])
    elif result1 != "BALANCED" and result2 == "BALANCED":
        result3 = animate_weighing("WEIGHING 3", [7], [8])
    else:
        result3 = animate_weighing("WEIGHING 3", [1], [2])
    
    # Final result
    time.sleep(2)
    print("\n" + "=" * 40)
    print("🎉 SOLUTION FOUND! 🎉")
    print(f"💰 The fake coin is: Coin {FAKE_COIN}")
    print(f"⚖️  It is: {FAKE_TYPE.upper()}")
    print("=" * 40)

if __name__ == "__main__":
    solve_twelve_coins_animated()