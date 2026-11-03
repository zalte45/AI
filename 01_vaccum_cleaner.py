# Initial condition of rooms
A = "Dirty"
B = "Dirty"

# Start in room A
room = "A"

while True:

    # Check current room
    if room == "A":
        if A == "Dirty":
            print("Room A: SUCK")
            A = "Clean"
        else:
            print("MOVE RIGHT")
            room = "B"

    else:
        if B == "Dirty":
            print("Room B: SUCK")
            B = "Clean"
        else:
            print("MOVE LEFT")
            room = "A"

    # Stop when both rooms are clean
    if A == "Clean" and B == "Clean":
        print("Both Rooms Clean")
        break
