"""Practical 3: Solve the 8-puzzle using A* search.

The blank tile is represented by 0. A* chooses the state with the smallest
f(n) = g(n) + h(n), where g is the moves so far and h is Manhattan distance.
Manhattan distance adds each numbered tile's row/column distance from its goal.

Run: python 03_astar_8_puzzle.py
Requires: Python standard library only (heapq).
"""

import heapq


def manhattan_distance(state, goal):
    """Estimate remaining moves by summing Manhattan distances of numbered tiles."""
    distance = 0
    for index, tile in enumerate(state):
        if tile == 0:  # The blank tile is not counted.
            continue

        current_row, current_col = divmod(index, 3)
        goal_index = goal.index(tile)
        goal_row, goal_col = divmod(goal_index, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    """Return all states reachable by moving the blank one square."""
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right.

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = (
                new_state[new_index], new_state[zero_index]
            )
            neighbors.append(tuple(new_state))

    return neighbors


def a_star(initial, goal):
    """Return the list of states from initial to goal, or None if not found."""
    # Heap entries: (f score, g score, current state, path before current state).
    priority_queue = [(manhattan_distance(initial, goal), 0, initial, [])]
    best_g = {initial: 0}

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)

        # Ignore an outdated heap entry if a better route was already found.
        if g != best_g.get(current):
            continue

        if current == goal:
            return path + [current]

        for neighbor in get_neighbors(current):
            new_g = g + 1
            if new_g < best_g.get(neighbor, float("inf")):
                best_g[neighbor] = new_g
                new_h = manhattan_distance(neighbor, goal)
                heapq.heappush(
                    priority_queue,
                    (new_g + new_h, new_g, neighbor, path + [current]),
                )

    return None


def print_state(state):
    """Display a flat 9-item state as a 3x3 board."""
    for index in range(0, 9, 3):
        print(state[index:index + 3])
    print()


if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    solution = a_star(initial_state, goal_state)
    if solution:
        print("Solution Found!")
        print("Number of moves:", len(solution) - 1)
        for step, state in enumerate(solution):
            print("Step", step)
            print_state(state)
    else:
        print("No solution found.")
