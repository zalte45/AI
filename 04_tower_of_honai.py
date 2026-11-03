from collections import deque

# Function to solve Tower of Hanoi using BFS
def solve(start, goal):

    # Initialize queue with initial state
    q = deque([start])

    # Store parent of each state
    parent = {start: None}

    # Continue until queue is empty
    while q:

        # Remove the first state from queue
        s = q.popleft()

        # Check whether goal state is reached
        if s == goal:

            # Store solution path
            path = []

            # Trace back from goal to start
            while s is not None:
                path.append(s)
                s = parent[s]

            # Reverse path to get start-to-goal order
            return path[::-1]

        # Select source rod
        for i in range(3):

            # Select destination rod
            for j in range(3):

                # Check valid disk movement
                if i != j and s[i] and (not s[j] or s[j][-1] > s[i][-1]):

                    # Copy current state into a list
                    a = [list(x) for x in s]

                    # Move top disk from source to destination
                    a[j].append(a[i].pop())

                    # Convert new state into tuple
                    t = tuple(tuple(x) for x in a)

                    # Check whether state is already visited
                    if t not in parent:

                        # Store parent state
                        parent[t] = s

                        # Add new state to queue
                        q.append(t)

    # Return empty path if no solution exists
    return []


# Fix number of disks to 3
n = 3

# Define initial state
start = (tuple(range(n, 0, -1)), (), ())

# Define goal state
goal = ((), (), tuple(range(n, 0, -1)))

# Display initial and goal states
print("Initial State:", start)
print("Goal State:", goal)

# Call solve function
path = solve(start, goal)

# Print solution path
print("\nSolution Path:")
for step, s in enumerate(path):
    print("Step", step, ":", s)

# Print total number of moves
print("Total Moves:", len(path) - 1)

