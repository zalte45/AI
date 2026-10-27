"""Practical 4: Tower of Hanoi using recursion and state tracking.

Move all disks from rod A to rod C using rod B. Only one disk can be moved
at a time, and a larger disk may never be placed on a smaller disk.
Minimum moves for n disks = 2**n - 1.

Run: python 04_tower_of_hanoi.py
Choose menu option 1, enter a positive number of disks, then choose option 4.
"""


class TowerOfHanoi:
    def __init__(self):
        self.reset()

    def reset(self):
        """Clear the puzzle and all stored state history."""
        self.n = 0
        self.rods = {}
        self.state_history = []
        self.moves = 0
        self.move_history = []
        self.solved = False

    def initialize(self, n):
        """Create a fresh puzzle with all disks stacked on rod A."""
        self.n = n
        self.moves = 0
        self.move_history = []
        self.rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
        self.state_history = []
        self.solved = False
        self.save_state()

    def save_state(self):
        """Save a copy of each rod after a move."""
        state = (self.rods['A'][:], self.rods['B'][:], self.rods['C'][:])
        self.state_history.append(state)

    def display_rods(self):
        print("\n-------------------------")
        print("      Current State")
        print("-------------------------")
        print("A (Source):", self.rods['A'])
        print("B (Auxiliary):", self.rods['B'])
        print("C (Destination):", self.rods['C'])

    def move_disk(self, source, destination):
        """Move the top disk from one rod to another and record the move."""
        disk = self.rods[source].pop()
        self.rods[destination].append(disk)
        self.moves += 1
        self.move_history.append((disk, source, destination))
        print("Move Disk", disk, ":", source, "->", destination)
        self.save_state()
        self.display_rods()

    def solve(self, n, source, auxiliary, destination):
        """Recursively move n disks from source to destination."""
        if n == 0:
            return
        if n == 1:
            self.move_disk(source, destination)
            return

        # First move the top n-1 disks out of the way.
        self.solve(n - 1, source, destination, auxiliary)
        # Move the largest remaining disk to the destination.
        self.move_disk(source, destination)
        # Move the n-1 disks onto the largest disk.
        self.solve(n - 1, auxiliary, source, destination)

    def show_initial_state(self):
        print("\n========== INITIAL STATE ==========")
        print("A:", list(range(self.n, 0, -1)))
        print("B:", [])
        print("C:", [])

    def show_goal_state(self):
        print("\n========== GOAL STATE ==========")
        print("A:", [])
        print("B:", [])
        print("C:", list(range(self.n, 0, -1)))

    def show_search_path(self):
        print("\n========== STATE SPACE SEARCH PATH ==========")
        for index, state in enumerate(self.state_history):
            print(f"\nState {index}")
            print("A:", state[0])
            print("B:", state[1])
            print("C:", state[2])

    def statistics(self):
        print("\n========== SEARCH SUMMARY ==========")
        print("Number of Disks:", self.n)
        print("Total States Generated:", len(self.state_history))
        print("State Transitions:", self.moves)
        print("Minimum Moves:", (2 ** self.n) - 1)
        print("Path Cost:", self.moves)
        print("Goal State:", "Reached" if self.solved else "Not Reached")


def menu():
    game = TowerOfHanoi()
    while True:
        print("\n" + "=" * 55)
        print(" TOWER OF HANOI USING STATE SPACE SEARCH ")
        print("=" * 55)
        print("1. Enter Number of Disks")
        print("2. Show Initial State")
        print("3. Show Goal State")
        print("4. Solve Tower of Hanoi")
        print("5. Show State Space Search Path")
        print("6. Show Search Statistics")
        print("7. Reset Puzzle")
        print("8. Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            try:
                n = int(input("Enter Number of Disks: "))
                if n <= 0:
                    print("Please enter a positive number.")
                    continue
                game.initialize(n)
                print("Puzzle Initialized Successfully.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice in (2, 3, 4, 5, 6) and game.n == 0:
            print("Please initialize the puzzle first.")
        elif choice == 2:
            game.show_initial_state()
        elif choice == 3:
            game.show_goal_state()
        elif choice == 4:
            if game.solved:
                print("Puzzle is already solved. Initialize a new puzzle to solve again.")
            else:
                print("\nGenerating Solution...\n")
                game.solve(game.n, 'A', 'B', 'C')
                game.solved = True
                print("Goal State Reached Successfully.")
        elif choice == 5:
            game.show_search_path()
        elif choice == 6:
            game.statistics()
        elif choice == 7:
            game.reset()
            print("Puzzle Reset Successfully.")
        elif choice == 8:
            print("Thank You!")
            break
        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    menu()
