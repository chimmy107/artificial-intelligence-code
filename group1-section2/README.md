# Group 1 Section 2 - AI Assignment

This folder contains the work for Group 1 Section 2.

## Members
- Henrietta Nwagwu - 20230838
- KingDavid - 20232634
- Caiaphas Adah Ebit - 20231052
- Babatobi Oluwafemi Ojo - 241030214
- Uanikhoba Deborah Olohije - 20232020
- Anjolaoluwa Adegbola Samuel - 20230865
- Isah Abubakar Sadiq - 20222335

## Assignment: The 12 Coins Problem

### What is the 12 Coin Problem?
Imagine you have 12 identical-looking coins, but one of them is fake. The fake coin looks exactly the same as the real ones, but it weighs slightly differently - it could be either heavier OR lighter than a real coin. You don't know which one is fake, and you don't know if it's heavier or lighter.

Your challenge: **Find the fake coin and determine if it's heavier or lighter using only a balance scale, and you can only use it 3 times maximum.**

### Why is this interesting?
This is a classic problem in artificial intelligence and logic because:
- There are 24 possible answers (12 coins × 2 possibilities each: heavy or light)
- Each weighing has 3 possible outcomes (left heavier, right heavier, or balanced)
- With 3 weighings, we can distinguish between 3³ = 27 different possibilities
- So we have just enough information to solve it!

### How our solution works:
1. **First weighing**: We compare 4 coins against 4 other coins
2. **Second weighing**: Based on the first result, we strategically choose which coins to compare
3. **Third weighing**: We narrow it down to the exact fake coin and whether it's heavy or light

Our Python implementation demonstrates this algorithm step-by-step, showing how the balance scale tips and how we use the information to solve the puzzle.

## Files
- `twelve_coin_problem.py` - Original animated version (requires matplotlib)
- `twelve_coin_simple.py` - Simple text-based version
- `twelve_coin_text_animation.py` - Animated text version with visual balance beam
- `twelve_coin_final.py` - Complete solution with detailed analysis
- `twelve_coin_test.py` - Tests multiple scenarios

## Instructions
Run any of the Python files to see the 12 Coins Problem solution in action:
```bash
python3 twelve_coin_text_animation.py  # For animated version
python3 twelve_coin_final.py          # For detailed analysis
```

The algorithm will show you step-by-step how to find the fake coin in exactly 3 weighings!