class VacuumCleaner:
    def __init__(self):
        self.environment = {
            "A": input("Is Room A Dirty or Clean? (Enter 'Dirty' or 'Clean'): "),
            "B": input("Is Room B Dirty or Clean? (Enter 'Dirty' or 'Clean'): ")
        }

    def reflex_agent(self):
        current_room = "A"

        while True:
            print("\nCurrent Environment")
            for room, status in self.environment.items():
                print(room, ":", status)

            if self.environment[current_room] == "Dirty":
                print("Action: SUCK")
                self.environment[current_room] = "Clean"

            else:
                if current_room == "A":
                    print("Action: MOVE RIGHT")
                    current_room = "B"
                else:
                    print("Action: MOVE LEFT")
                    current_room = "A"

            if self.environment["A"] == "Clean" and self.environment["B"] == "Clean":
                print("\nEnvironment Completely Clean.")
                break


vacuum = VacuumCleaner()
vacuum.reflex_agent()
