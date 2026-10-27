"""Practical 5: Solve the 8-puzzle using Breadth-First Search (BFS).

BFS explores states in increasing number of moves. The blank tile is 0.
Each queue entry stores a board state and the moves taken to reach it.
For an unweighted puzzle, BFS finds a solution with the fewest moves.

Run: python 05_bfs_8_puzzle.py
"""

from collections import deque


def print_state(state):
    """Print the 9-tile tuple as a 3x3 board."""
    for index in range(0, 9, 3):
        print(state[index:index + 3])
    print()


def get_neighbors(state):
    """Generate each legal board state by moving the blank tile."""
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)
    moves = {
        "Up": (-1, 0),
        "Down": (1, 0),
        "Left": (0, -1),
        "Right": (0, 1),
    }

    for move, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank], new_state[new_blank] = (
                new_state[new_blank], new_state[blank]
            )
            neighbors.append((tuple(new_state), move))

    return neighbors


def bfs(initial, goal):
    """Return the shortest sequence of (move, resulting_state), or None."""
    queue = deque([(initial, [])])
    visited = {initial}  # Mark states when enqueued to avoid duplicates.

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path

        for next_state, move in get_neighbors(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(move, next_state)]))

    return None


if __name__ == "__main__":
    initial_state = (1, 2, 3, 5, 6, 4, 7, 8, 0)
    goal_state = (1, 2, 3, 5, 6, 0, 7, 8, 4)

    solution = bfs(initial_state, goal_state)
    print("Initial State:")
    print_state(initial_state)

    if solution is not None:
        print("Solution Found!")
        print("Number of moves:", len(solution))
        for step, (move, state) in enumerate(solution, start=1):
            print("Step", step, "- Move:", move)
            print_state(state)
    else:
        print("No solution found.")
