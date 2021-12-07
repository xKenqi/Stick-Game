print("Welcome to the Game of Sticks.")
print("Please enter your name to begin.")
print("Keep in mind player 1 goes first. ")
player1 = input("Please enter your name player 1: ")
player2 = input("Please enter your name player 2: ")
sticks = 15
player1turn = True
player2turn = False
while sticks > 0:
    while player1turn == True:
        remove = int(input("How many sticks would you like to remove Player 1? " ))
        if remove > 3:
            print("You cannot remove more than 3 sticks at a time.")
        elif sticks > remove:
            sticks = sticks - remove
            print("There are", sticks, "sticks remaining.")
            player1turn = False
            player2turn = True
        elif sticks < remove:
            print("Not enough sticks, try again.")
        elif sticks == remove:
            sticks = sticks - remove
            print("Winner:", player2)
            player2turn = False
            player1turn = False
            break
    while player2turn == True:
        remove = int(input("How many sticks would you like to remove Player 2? " ))
        if remove > 3:
            print("You cannot remove more than 3 sticks at a time.")
        elif sticks > remove:
            sticks = sticks - remove
            print("There are", sticks, "sticks remaining.")
            player1turn = True
            player2turn = False
        elif sticks < remove:
            print("Not enough sticks, try again.")
        elif sticks == remove:
            sticks = sticks - remove
            print("Winner:", player1)
            player2turn = False
            player1turn = False
            break

