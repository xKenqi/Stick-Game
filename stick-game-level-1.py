sticks = 15
while sticks > 0:
    remove = int(input("How many sticks would you like to remove?" ))
    if remove > 3:
        print("You cannot remove more than 3 sticks at a time.")
    elif sticks > remove:
        sticks = sticks - remove
        print("There are", sticks, "sticks remaining.")
    elif sticks < remove:
        print("Not enough sticks, try again.")
    elif sticks == remove:
        print("There are no sticks remaining.")
        break
