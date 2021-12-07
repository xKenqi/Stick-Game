import random
print("Welcome to the Game of Sticks.")
player = input("What is your prefered name?: ")
turn = input("Would you like to First or Second?: ")
sticks = 50
player1turn = False
StickBot = False
if turn == "First":
    player1turn = True
    StickBot = False
elif turn == "Second":
    player1turn = False
    StickBot = True
while sticks > 0:
    while player1turn == True:
        remove = int(input("How many sticks would you like to remove?: "))
        if remove > 3:
            print("Invalid amount of number. Only 3 or less amount of sticks allowed to remove at a time.")
        elif remove < sticks:
            sticks = sticks - remove
            print("There are", sticks, "sticks remaining.")
            player1turn = False
            StickBot = True
        elif remove > sticks:
            print("Invalid amount of number. Not enough sticks.")
        elif remove == sticks:
            sticks = sticks - remove
            print("StickBot Won.")
            print(player, "You Lost.")
            player1turn = False
            StickBot = False 
            break
    while StickBot == True:
        remove1 = random.randint(1,3)
        if sticks % 2 == 4:
            remove1 = 3
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks % 2 == 3:
            remove1 = 2
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks % 2 == 2:
            remove1 = 1
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 15:
            remove1 = 2
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 12:
            remove1 = 3
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 11:
            remove1 == 2
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 10:
            remove1 = 1
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 8:
            remove1 = 3
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 7:
            remove1 = 2
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 6:
            remove1 = 1
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 5:
            remove1 = 2
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 4:
            remove1 = 3
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 3:
            remove1 = 2
            sticks = sticks - remove1
            print("StickBot decided to remove",remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif sticks == 2:
            remove1 = 1
            sticks = sticks - remove1
            player1turn = True
            StickBot = False
            print("StickBot decided to remove",remove1,"stick(s).")
            print("There are",sticks, "stick(s) remaining.")
        elif remove1 < sticks:
            sticks = sticks - remove1
            print("StickBot decied to remove", remove1, "stick(s).")
            print("There are", sticks, "stick(s) remaining.")
            player1turn = True
            StickBot = False
        elif remove1 == sticks:
            sticks = sticks - remove1
            player1turn = False 
            StickBot = False
            print(player, "You Won.")
            print("StickBot Lost.")
            break
        
           

    


