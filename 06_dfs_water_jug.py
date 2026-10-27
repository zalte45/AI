"""Practical 6: Water Jug Problem using Depth-First Search (DFS).

Jug A holds 4 litres; Jug B holds 3 litres. Start with (0, 0), and reach
(2, 0): exactly 2 litres in A and 0 litres in B. Each state is (A, B).

Run: python 06_dfs_water_jug.py
"""


def get_next_states(state):
    """Return possible next states and the operation that causes each one."""
    a, b = state
    states = []

    # Fill either jug to capacity or empty either jug.
    states.append(((4, b), "Fill Jug A"))
    states.append(((a, 3), "Fill Jug B"))
    states.append(((0, b), "Empty Jug A"))
    states.append(((a, 0), "Empty Jug B"))

    # Pour from A into B until A is empty or B is full.
    transfer = min(a, 3 - b)
    states.append(((a - transfer, b + transfer), "Pour A -> B"))

    # Pour from B into A until B is empty or A is full.
    transfer = min(b, 4 - a)
    states.append(((a + transfer, b - transfer), "Pour B -> A"))

    return states


def dfs_water_jug():
    """Use a stack to search for a route from the initial state to the goal."""
    initial = (0, 0)
    goal = (2, 0)
    stack = [(initial, [initial])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)

        for next_state, operation in get_next_states(state):
            if next_state not in visited:
                # Store both the action and resulting state for readable output.
                stack.append((next_state, path + [operation, next_state]))

    return None


if __name__ == "__main__":
    solution = dfs_water_jug()
    if solution:
        print("Solution Found:")
        for item in solution:
            print(item)
    else:
        print("No solution found.")
