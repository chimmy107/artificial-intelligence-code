import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ROWS, COLS = 5, 4
GOAL_TOP_LEFT = (3, 1)

START = (
    (2, 1, 1, 3),
    (2, 1, 1, 3),
    (4, 6, 7, 5),
    (4, 8, 9, 5),
    (0,10,11,0),
)


def find_blocks(board):
    blocks = {}
    for r in range(ROWS):
        for c in range(COLS):
            v = board[r][c]
            if v != 0:
                blocks.setdefault(v, []).append((r, c))
    return blocks


def is_goal(board):
    red = find_blocks(board)[1]
    r0 = min(r for r, _ in red)
    c0 = min(c for _, c in red)
    return (r0, c0) == GOAL_TOP_LEFT


def can_move(board, cells, dr, dc):
    for r, c in cells:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < ROWS and 0 <= nc < COLS):
            return False
        if board[nr][nc] not in (0, board[r][c]):
            return False
    return True


def move(board, cells, dr, dc, bid):
    new = [list(row) for row in board]
    for r, c in cells:
        new[r][c] = 0
    for r, c in cells:
        new[r+dr][c+dc] = bid
    return tuple(tuple(row) for row in new)


def neighbors(board):
    result = []
    blocks = find_blocks(board)
    for bid, cells in blocks.items():
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            if can_move(board, cells, dr, dc):
                result.append(move(board, cells, dr, dc, bid))
    return result


def dfs(start):
    stack = [(start, [start])]
    visited = set()

    while stack:
        board, path = stack.pop()
        if board in visited:
            continue
        visited.add(board)

        if is_goal(board):
            return path

        for nb in neighbors(board):
            if nb not in visited:
                stack.append((nb, path + [nb]))

    return None


print("Solving with DFS...")
solution = dfs(START)
print("Moves:", len(solution) - 1)


#Animation

COLOURS = {
    0: "white",
    1: "red",
    2: "skyblue", 3: "skyblue",
    4: "skyblue", 5: "skyblue",
    6: "lightgreen", 7: "lightgreen",
    8: "orange", 9: "orange",
    10: "orange", 11: "orange",
}

fig, ax = plt.subplots()

def draw(board):
    ax.clear()
    ax.set_xlim(0, COLS)
    ax.set_ylim(ROWS, 0)
    ax.set_xticks(range(COLS))
    ax.set_yticks(range(ROWS))
    ax.grid(True)
    for r in range(ROWS):
        for c in range(COLS):
            ax.add_patch(
                plt.Rectangle(
                    (c, r), 1, 1,
                    facecolor=COLOURS[board[r][c]],
                    edgecolor="black"
                )
            )

def animate(i):
    draw(solution[i])
    ax.set_title(f"DFS Solution – Move {i}/{len(solution)-1}")

FuncAnimation(fig, animate, frames=len(solution), interval=300, repeat=False)
plt.show()


