import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from collections import deque
import copy

# Initial block positions
blocks_init = [
    (1, 0, 1, 2, 2),  # red 2x2
    (2, 0, 0, 2, 1),  # vertical left
    (2, 0, 3, 2, 1),  # vertical right
    (3, 2, 0, 1, 2),  # horizontal bottom-left
    (3, 2, 2, 1, 2),  # horizontal bottom-right
    (4, 3, 1, 1, 1),  # small bottom-left
    (4, 3, 2, 1, 1),  # small bottom-right
]

ROWS, COLS = 5, 4
GOAL_POS = (3, 1) 

def encode_state(blocks):
    """Encode blocks positions as a tuple for BFS visited set"""
    return tuple(sorted((b[0], b[1], b[2]) for b in blocks))

def is_goal(blocks):
    """Check if red 2x2 block reached goal"""
    for b in blocks:
        if b[0] == 1:  # red block
            return (b[1], b[2]) == GOAL_POS
    return False

def build_grid(blocks):
    """Create 2D grid from blocks"""
    grid = [[0]*COLS for _ in range(ROWS)]
    for b in blocks:
        id, r, c, h, w = b
        for i in range(h):
            for j in range(w):
                grid[r+i][c+j] = id
    return grid

def move_block(block, dr, dc, blocks):
    """Move a block if possible, return new blocks list or None"""
    id, r, c, h, w = block
    # check bounds
    if r+dr < 0 or r+dr+h > ROWS or c+dc < 0 or c+dc+w > COLS:
        return None
    # build grid
    grid = build_grid(blocks)
    # check collision
    for i in range(h):
        for j in range(w):
            nr, nc = r+i+dr, c+j+dc
            if grid[nr][nc] != 0 and grid[nr][nc] != id:
                return None
    # move block
    new_blocks = []
    for b in blocks:
        if b == block:
            new_blocks.append((id, r+dr, c+dc, h, w))
        else:
            new_blocks.append(b)
    return new_blocks

# BFS Solver

def bfs(blocks_init):
    visited = set()
    queue = deque([(blocks_init, [])])
    while queue:
        blocks, path = queue.popleft()
        state = encode_state(blocks)
        if state in visited:
            continue
        visited.add(state)

        if is_goal(blocks):
            return path + [blocks]

        for b in blocks:
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_blocks = move_block(b, dr, dc, blocks)
                if new_blocks:
                    queue.append((new_blocks, path + [blocks]))
    return None

# Solve
print("Solving Red Donkey puzzle...")
solution = bfs(blocks_init)
if solution:
    print(f"Solution found in {len(solution)-1} moves!")
else:
    print("No solution found!")

# Animation

fig, ax = plt.subplots()
ax.set_xlim(0, COLS)
ax.set_ylim(0, ROWS)
ax.set_aspect('equal')
ax.axis('off')
patches_list = []

colors = {1:'red', 2:'green', 3:'orange', 4:'blue'}

def draw_board(blocks):
    global patches_list
    for p in patches_list:
        p.remove()
    patches_list.clear()
    for b in blocks:
        id, r, c, h, w = b
        rect = patches.Rectangle((c, ROWS-1-r-h+1), w, h, facecolor=colors[id], edgecolor='black')
        ax.add_patch(rect)
        patches_list.append(rect)

def animate(i):
    draw_board(solution[i])
    ax.set_title(f"Move {i}/{len(solution)-1}")

if solution:
    anim = FuncAnimation(fig, animate, frames=len(solution), interval=200, repeat=False)
    plt.show()




