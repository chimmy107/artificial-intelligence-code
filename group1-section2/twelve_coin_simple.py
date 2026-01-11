# 12 Coins Problem – Recursive AI Solution (Text-based version)

# Hidden truth (for demonstration)
FAKE_COIN = 6
FAKE_TYPE = "light"  # "heavy" or "light"

def weight(coin):
    if coin != FAKE_COIN:
        return 1
    return 2 if FAKE_TYPE == "heavy" else 0

def weigh_coins(left, right):
    """Weigh two groups of coins and return the result"""
    left_weight = sum(weight(c) for c in left)
    right_weight = sum(weight(c) for c in right)
    
    if left_weight > right_weight:
        return "left_heavier"
    elif right_weight > left_weight:
        return "right_heavier"
    else:
        return "balanced"

def solve_twelve_coins():
    """Solve the 12 coins problem using 3 weighings"""
    print("=== 12 Coins Problem Solver ===")
    print(f"Fake coin: {FAKE_COIN} (type: {FAKE_TYPE})")
    print()
    
    # Step 1: First weighing
    print("Weighing 1: [1,2,3,4] vs [5,6,7,8]")
    result1 = weigh_coins([1,2,3,4], [5,6,7,8])
    print(f"Result: {result1}")
    
    if result1 == "balanced":
        # Fake coin is in [9,10,11,12]
        print("Weighing 2: [9,10] vs [1,2] (known good coins)")
        result2 = weigh_coins([9,10], [1,2])
        print(f"Result: {result2}")
        
        if result2 == "balanced":
            # Fake coin is in [11,12]
            print("Weighing 3: [11] vs [1] (known good coin)")
            result3 = weigh_coins([11], [1])
            print(f"Result: {result3}")
            
            if result3 == "balanced":
                print("Coin 12 is fake!")
            elif result3 == "left_heavier":
                print("Coin 11 is fake and heavy!")
            else:
                print("Coin 11 is fake and light!")
        else:
            # Fake coin is in [9,10]
            print("Weighing 3: [9] vs [1] (known good coin)")
            result3 = weigh_coins([9], [1])
            print(f"Result: {result3}")
            
            if result3 == "balanced":
                print("Coin 10 is fake!")
            elif result3 == "left_heavier":
                print("Coin 9 is fake and heavy!")
            else:
                print("Coin 9 is fake and light!")
    
    elif result1 == "left_heavier":
        # Fake coin is in [1,2,3,4] (heavy) or [5,6,7,8] (light)
        print("Weighing 2: [1,2,5] vs [3,6,9]")
        result2 = weigh_coins([1,2,5], [3,6,9])
        print(f"Result: {result2}")
        
        if result2 == "balanced":
            # Fake coin is in [4,7,8]
            print("Weighing 3: [7] vs [8]")
            result3 = weigh_coins([7], [8])
            print(f"Result: {result3}")
            
            if result3 == "balanced":
                print("Coin 4 is fake and heavy!")
            elif result3 == "left_heavier":
                print("Coin 7 is fake and light!")
            else:
                print("Coin 8 is fake and light!")
        elif result2 == "left_heavier":
            # Fake coin is in [1,2] (heavy) or [6] (light)
            print("Weighing 3: [1] vs [2]")
            result3 = weigh_coins([1], [2])
            print(f"Result: {result3}")
            
            if result3 == "balanced":
                print("Coin 6 is fake and light!")
            elif result3 == "left_heavier":
                print("Coin 1 is fake and heavy!")
            else:
                print("Coin 2 is fake and heavy!")
        else:
            # Fake coin is in [3] (heavy) or [5] (light)
            print("Weighing 3: [3] vs [9] (known good coin)")
            result3 = weigh_coins([3], [9])
            print(f"Result: {result3}")
            
            if result3 == "balanced":
                print("Coin 5 is fake and light!")
            elif result3 == "left_heavier":
                print("Coin 3 is fake and heavy!")
            else:
                print("Something went wrong!")
    
    else:  # right_heavier
        # Fake coin is in [1,2,3,4] (light) or [5,6,7,8] (heavy)
        print("Weighing 2: [1,2,5] vs [3,6,9]")
        result2 = weigh_coins([1,2,5], [3,6,9])
        print(f"Result: {result2}")
        
        if result2 == "balanced":
            # Fake coin is in [4,7,8]
            print("Weighing 3: [7] vs [8]")
            result3 = weigh_coins([7], [8])
            print(f"Result: {result3}")
            
            if result3 == "balanced":
                print("Coin 4 is fake and light!")
            elif result3 == "left_heavier":
                print("Coin 8 is fake and heavy!")
            else:
                print("Coin 7 is fake and heavy!")
        elif result2 == "left_heavier":
            # Fake coin is in [3] (light) or [5] (heavy)
            print("Weighing 3: [3] vs [9] (known good coin)")
            result3 = weigh_coins([3], [9])
            print(f"Result: {result3}")
            
            if result3 == "balanced":
                print("Coin 5 is fake and heavy!")
            elif result3 == "left_heavier":
                print("Something went wrong!")
            else:
                print("Coin 3 is fake and light!")
        else:
            # Fake coin is in [1,2] (light) or [6] (heavy)
            print("Weighing 3: [1] vs [2]")
            result3 = weigh_coins([1], [2])
            print(f"Result: {result3}")
            
            if result3 == "balanced":
                print("Coin 6 is fake and heavy!")
            elif result3 == "left_heavier":
                print("Coin 2 is fake and light!")
            else:
                print("Coin 1 is fake and light!")

if __name__ == "__main__":
    solve_twelve_coins()