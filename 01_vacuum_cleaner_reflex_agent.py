# Simple Reflex Agent - Vacuum Cleaner
# The agent cleans two rooms: A and B.

class VacuumCleaner:

    # Initialize the environment
    def __init__(self):
        self.environment = {
            "A": "Dirty",
            "B": "Dirty"
        }

    # Display the current condition of both rooms
    def display(self):
        print("\nCurrent Environment")

        for room in self.environment:
            print(room, ":", self.environment[room])

    # Implement the reflex agent
    def reflex_agent(self):
        current_room = "A"

        while True:

            # Display the current environment
            self.display()

            # If the current room is dirty, clean it
            if self.environment[current_room] == "Dirty":
                print("Action: SUCK")
                self.environment[current_room] = "Clean"

            else:
                # If the agent is in room A, move to room B
                if current_room == "A":
                    print("Action: MOVE RIGHT")
                    current_room = "B"

                # If the agent is in room B, move to room A
                else:
                    print("Action: MOVE LEFT")
                    current_room = "A"

            # Stop when both rooms are clean
            if (self.environment["A"] == "Clean" and
                    self.environment["B"] == "Clean"):

                print("\nEnvironment Completely Clean.")
                break


# Create the vacuum cleaner object
vacuum = VacuumCleaner()

# Start the reflex agent
vacuum.reflex_agent()

