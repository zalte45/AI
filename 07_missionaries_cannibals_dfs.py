"""Practical 7: Missionaries and Cannibals using DFS.

There are 3 missionaries and 3 cannibals. The boat carries one or two people.
On either bank, cannibals may not outnumber missionaries if any missionaries
are present. State format: (missionaries_left, cannibals_left, boat_side).
Boat side is 'L' or 'R'.

Run: python 07_missionaries_cannibals_dfs.py
"""


def is_valid(state):
    """Check people counts and the safety rule on both river banks."""
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False
    if boat not in ('L', 'R'):
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True


def generate_states(state):
    """List valid next states and the crossing action from the current state."""
    m_left, c_left, boat = state
    moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]
    next_states = []

    for m, c in moves:
        if boat == 'L':
            # Passengers leave the left bank and arrive at the right bank.
            new_state = (m_left - m, c_left - c, 'R')
            action = f"Send {m}M {c}C L->R"
        else:
            # Passengers return from the right bank to the left bank.
            new_state = (m_left + m, c_left + c, 'L')
            action = f"Return {m}M {c}C R->L"

        # Reject moves that would create invalid counts or unsafe banks.
        if is_valid(new_state):
            # Also reject a move if it tries to move more people than are on
            # the boat's current bank. The count checks above catch this too.
            next_states.append((new_state, action))

    return next_states


def dfs_missionaries_cannibals():
    """Search the state space with a stack and return the found route."""
    initial = (3, 3, 'L')
    goal = (0, 0, 'R')
    stack = [(initial, [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path + [(state, "Goal Reached")]
        if state in visited:
            continue
        visited.add(state)

        for next_state, action in generate_states(state):
            if next_state not in visited:
                stack.append((next_state, path + [(state, action)]))

    return None


if __name__ == "__main__":
    solution = dfs_missionaries_cannibals()
    if solution:
        print("Solution Found:\n")
        for state, action in solution:
            print(state, "->", action)
    else:
        print("No solution found.")
