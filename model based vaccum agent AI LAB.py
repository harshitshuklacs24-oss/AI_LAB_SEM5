# Model-Based Vacuum Cleaner Agent

# Initial environment
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

# Agent's internal model
model = {
    "A": "Unknown",
    "B": "Unknown"
}

location = "A"

while "Dirty" in model.values() or "Unknown" in model.values():

    # Sense the current room
    percept = environment[location]

    # Update internal model
    model[location] = percept

    print("Current location:", location)
    print("Room status:", percept)

    # Take action
    if percept == "Dirty":
        print("Action: Suck")
        environment[location] = "Clean"
        model[location] = "Clean"

    else:
        print("Action: Move")

    # Move to the other room if it is not finished
    if "Dirty" in model.values() or "Unknown" in model.values():
        location = "B" if location == "A" else "A"

print("\nAll rooms are clean!")