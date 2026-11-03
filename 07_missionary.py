# Check whether the current state is valid or not
def is_valid(state):

    # Get missionaries, cannibals on left bank and boat position
    m_left, c_left, boat = state

    # Calculate people on the right bank
    m_right = 3 - m_left
    c_right = 3 - c_left

    # Check that people counts are between 0 and 3
    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

    # Boat must be either on the Left or Right bank
    if boat not in ('L', 'R'):
        return False

    # Missionaries must not be outnumbered by cannibals on left bank
    if m_left > 0 and m_left < c_left:
        return False

    # Missionaries must not be outnumbered by cannibals on right bank
    if m_right > 0 and m_right < c_right:
        return False

    # If all conditions are valid, return True
    return True


# Generate all possible valid next states
def generate_states(state):

    # Get current state details
    m_left, c_left, boat = state

    # Possible boat passenger combinations
    moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]

    # Store valid next states
    next_states = []

    # Check each possible move
    for m, c in moves:

        # If boat is on the left bank
        if boat == 'L':

            # Move people from left bank to right bank
            new_state = (m_left - m, c_left - c, 'R')

            # Store the action
            action = f"Send {m}M {c}C L->R"

        # If boat is on the right bank
        else:

            # Move people from right bank to left bank
            new_state = (m_left + m, c_left + c, 'L')

            # Store the action
            action = f"Return {m}M {c}C R->L"

        # Check whether the new state is safe and valid
        if is_valid(new_state):

            # Add valid state and action to the list
            next_states.append((new_state, action))

    # Return all valid next states
    return next_states


# Solve the problem using Depth-First Search
def dfs_missionaries_cannibals():

    # Initial state: all people and boat are on the left bank
    initial = (3, 3, 'L')

    # Goal state: all people are on the right bank
    goal = (0, 0, 'R')

    # Stack stores the current state and path
    stack = [(initial, [])]

    # Set stores already visited states
    visited = set()

    # Continue until the stack becomes empty
    while stack:

        # Remove the last state from the stack (LIFO)
        state, path = stack.pop()

        # If goal is reached, return the solution path
        if state == goal:
            return path + [(state, "Goal Reached")]

        # Skip states that are already visited
        if state in visited:
            continue

        # Mark current state as visited
        visited.add(state)

        # Generate possible next states
        for next_state, action in generate_states(state):

            # Process only unvisited states
            if next_state not in visited:

                # Add new state and action to the stack
                stack.append((next_state, path + [(state, action)]))

    # Return None if no solution is found
    return None


# Main program starts here
if __name__ == "__main__":

    # Call the DFS function
    solution = dfs_missionaries_cannibals()

    # If solution exists
    if solution:

        # Print solution
        print("Solution Found:\n")

        # Print each state and action
        for state, action in solution:
            print(state, "->", action)

    # If no solution exists
    else:
        print("No solution found.")
