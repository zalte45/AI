from collections import deque

# BFS function
def bfs(start, goal):
    q = deque([(start, [])])
    visited = set()

    while q:
        state, path = q.popleft()

        # Check goal state
        if state == goal:
            return path + [state]

        # Check visited state
        if state not in visited:
            visited.add(state)

            # Find blank tile
            i = state.index(0)

            # Generate possible moves
            for j in [i + 3, i - 3, i + 1, i - 1]:

                # Check valid movement
                if 0 <= j < 9 and (i // 3 == j // 3 or i % 3 == j % 3):

                    # Swap blank tile
                    new = list(state)
                    new[i], new[j] = new[j], new[i]

                    # Add new state to queue
                    q.append((tuple(new), path + [state]))

    return None


# Initial and goal states
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Call BFS
result = bfs(start, goal)

# Print solution
if result:
    print("Solution Found")
    print("Number of Moves:", len(result) - 1)

    for step, state in enumerate(result):
        print(f"\nStep: {step}")
        print(state[:3])
        print(state[3:6])
        print(state[6:])

else:
    print("No solution")