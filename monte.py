import random

ALL_CLOSED = """
+-------+   +-------+   +-------+
|       |   |       |   |       |
|   1   |   |   2   |   |   3   |
|       |   |       |   |       |
|       |   |       |   |       |
|       |   |       |   |       |
+-------+   +-------+   +-------+"""
FIRST_GOAT = """
+-------+   +-------+   +-------+
|   ((  |   |       |   |       |
|   OO  |   |   2   |   |   3   |
|  /_/|_|   |       |   |       |
|     | |   |       |   |       |
|GOAT |||   |       |   |       |
+-------+   +-------+   +-------+"""
SECOND_GOAT = """
+-------+   +-------+   +-------+
|       |   |   ((  |   |       |
|   1   |   |   OO  |   |   3   |
|       |   |  /_/|_|   |       |
|       |   |     | |   |       |
|       |   |GOAT |||   |       |
+-------+   +-------+   +-------+"""
THIRD_GOAT = """
+-------+   +-------+   +-------+
|       |   |       |   |   ((  |
|   1   |   |   2   |   |   OO  |
|       |   |       |   |  /_/|_|
|       |   |       |   |     | |
|       |   |       |   |GOAT |||
+-------+   +-------+   +-------+"""
FIRST_CAR = """
+-------+   +-------+   +-------+
|       |   |   ((  |   |   ((  |
|    ___|   |   OO  |   |   OO  |
|  _/   |   |  /_/|_|   |  /_/|_|
| /_____|   |     | |   |     | |
|   0   |   |GOAT |||   |GOAT |||
+-------+   +-------+   +-------+"""
SECOND_CAR = """
+-------+   +-------+   +-------+
|   ((  |   |       |   |   ((  |
|   OO      |    ___|   |   OO  |
|  /_/|_|   |  _/   |   |  /_/|_|  
|     | |   | /_____|   |     | |
|GOAT |||   |   0   |   |GOAT |||
+-------+   +-------+   +-------+"""
THIRD_CAR = """
+-------+   +-------+   +-------+
|   ((  |   |   ((  |   |       |  
|   OO  |   |   OO      |    ___|  
|  /_/|_|   |  /_/|_|   |  _/   |      
|     | |   |     | |   | /_____|  
|GOAT |||   |GOAT |||   |   0   |  
+-------+   +-------+   +-------+   """


while True:
    wining_door = random.randint(1, 3)
    goats = [1, 2, 3]
    choices = [1, 2, 3]
    goats.remove(wining_door)

    print("\nThis is the Monte Hall Problem. There is a car behind one of the doors and a goat behind the other two.")
    print(ALL_CLOSED)

    # Player makes their first choice
    choice = int(input("Which door would you like to pick? >> "))
    
    # Check if the choice is valid
    if choice not in [1, 2, 3]:
        print("Are you dumb? Just choose 1, 2, or 3.")
        continue  # Restart the loop if input is invalid
    
    # Monty reveals a goat behind a door the player didn't choose
    if choice != wining_door:
        reveal = random.choice(goats)
    else:
        for door in goats:
            if door != choice:
                reveal = door

    choices.remove(reveal)

    # Display the door Monty reveals
    if reveal == 1:
        print(FIRST_GOAT)
        print("There is a goat behind door number 1.")
    elif reveal == 2:
        print(SECOND_GOAT)
        print("There is a goat behind door number 2.")
    else:
        print(THIRD_GOAT)
        print("There is a goat behind door number 3.")

    # Ask player if they want to switch
    switch = input("Would you like to (k)eep your choice or (s)witch? >> ").lower()
    if switch == "s":
        choice = choices[0]

    # Reveal the outcome
    if wining_door == 1:
        print(FIRST_CAR)
    elif wining_door == 2:
        print(SECOND_CAR)
    else:
        print(THIRD_CAR)

    if choice == wining_door:
        print("You win a brand new car!")
    else:
        print("You win a goat!")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (y/n) >> ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
