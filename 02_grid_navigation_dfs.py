"""Practical 2: Grid navigation with obstacles using Depth-First Search (DFS).

Note: The source file calls this a model-based agent, but the implemented
search algorithm is DFS. The visited set stores explored cells; this is not,
by itself, a full model-based agent architecture.

Grid symbols: S = start, G = goal, X = obstacle, . = free cell.
Moves are attempted in this order: right, down, left, up.

Run: python 02_grid_navigation_dfs.py
"""

# A 5x5 map. The agent may not enter cells marked X.
# Model-Based Intelligent Agent
# Grid Navigation with Obstacles using DFS

# Create a 5x5 grid
# S = Starting position
# G = Goal position
# X = Obstacle
# '' = Empty cell

grid = [
    ['S', '', '', '', ''],
    ['', 'X', '', 'X', ''],
    ['', '', '', '', ''],
    ['X', '', 'X', '', ''],
    ['', '', '', '', 'G']
]

# Calculate the number of rows and columns
rows = len(grid)
cols = len(grid[0])

# Define the starting and goal positions
start = (0, 0)
goal = (4, 4)

# Store visited cells to avoid revisiting them
visited = set()

# Possible movements: Right, Down, Left, Up
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# Check whether a cell is valid
def is_valid(x, y):
    return (
        0 <= x < rows and
        0 <= y < cols and
        grid[x][y] != 'X' and
        (x, y) not in visited
    )


# Perform Depth-First Search
def dfs(position):
    x, y = position

    # Check whether the agent has reached the goal
    if position == goal:
        print("Goal Reached!")
        return True

    # Mark the current position as visited
    visited.add(position)

    # Display the agent's current position
    print("Agent at:", position)

    # Explore all possible movements
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        # Move only if the next cell is valid
        if is_valid(nx, ny):
            if dfs((nx, ny)):
                return True

    # Return False if no path to the goal is found
    return False


# Display the grid environment
print("Grid Environment")

for row in grid:
    print(row)

# Start navigation
print("\nNavigation Starts\n")

dfs(start)

# Display all visited cells
print("\nVisited Cells")
print(visited)
