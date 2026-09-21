# Simple Vacuum Cleaner Program

room = {
    "A": "Dirty",
    "B": "Dirty"
}

position = "A"

while True:
    print("Current position:", position)
    print("Room status:", room)

    if room[position] == "Dirty":
        print("Cleaning room...")
        room[position] = "Clean"
    else:
        print("Room is already clean.")

    if position == "A":
        position = "B"
    else:
        position = "A"

    if room["A"] == "Clean" and room["B"] == "Clean":
        print("Both rooms are clean!")
        break
