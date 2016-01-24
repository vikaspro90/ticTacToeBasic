# Just run the file to play the game against the computer

import random                                                                  # Added by vpalakur
import time                                                                    # Added by vpalakur

#This function is to print the Tic Tac Toe board

def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""

#This function checks whether or not the game is complete

def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print_board()
            print
            if flag == "c":                                                    # Added by vpalakur : To check if the last move was by the player or the computer
                print "I win... Better luck next time... :)"                   # Added by vpalakur
            else:                                                              # Added by vpalakur
                print "You win.. good game... I should try better..."          # Added by vpalakur

            return True
        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        print_board()
        print
        if flag == "c":
            print "I win... Better luck next time... :)"
        else:
            print "You win.. good game... I should try better..."
        return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print_board()
        print
        print "It is a draw... We are equally smart.. Are you a computer too..!!!"
        return True

    return False

# The below function has the logic using which the computer makes a move - Added by vpalakur

def make_move():
    corners = [1,3,7,9]
    sides = [2,4,6,8]

    #1. The below logic is to check if com has two in a row, and if yes, make a move to win the game

    movedc = False
    for a in range(0,3):
        if movedc == True:
            break
        if map[a][0] == map[a][1] == com and map[a][2] == " ":
            map[a][2] = com
            movedc = True
        elif map[a][1] == map[a][2] == com and map[a][0] == " ":
            map[a][0] = com
            movedc = True
        elif map[a][0] == map[a][2] == com and map[a][1] == " ":
            map[a][1] = com
            movedc = True
        elif map[0][a] == map[1][a] == com and map[2][a] == " ":
            map[2][a] = com
            movedc = True
        elif map[1][a] == map[2][a] == com and map[0][a] == " ":
            map[0][a] = com
            movedc = True
        elif map[0][a] == map[2][a] == com and map[1][a] == " ":
            map[1][a] = com
            movedc = True

    if movedc == False:
        if map[0][0] == map[1][1] == com and map[2][2] == " ":
            map[2][2] = com
            movedc = True
        elif map[1][1] == map[2][2] == com and map[0][0] == " ":
            map[0][0] = com
            movedc = True
        elif map[2][2] == map[0][0] == com and map[1][1] == " ":
            map[1][1] = com
            movedc = True
        elif map[2][0] == map[1][1] == com and map[0][2] == " ":
            map[0][2] = com
            movedc = True
        elif map[1][1] == map[0][2] == com and map[2][0] == " ":
            map[2][0] = com
            movedc = True
        elif map[0][2] == map[2][0] == com and map[1][1] == " ":
            map[1][1] = com
            movedc = True

    #2. The below logic is to check if player has two in a row, if yes, then block the player
    
    for a in range(0,3):
        if movedc == True:
            break
        if map[a][0] == map[a][1] == player and map[a][2] == " ":
            map[a][2] = com
            movedc = True
        elif map[a][1] == map[a][2] == player and map[a][0] == " ":
            map[a][0] = com
            movedc = True
        elif map[a][0] == map[a][2] == player and map[a][1] == " ":
            map[a][1] = com
            movedc = True
        elif map[0][a] == map[1][a] == player and map[2][a] == " ":
            map[2][a] = com
            movedc = True
        elif map[1][a] == map[2][a] == player and map[0][a] == " ":
            map[0][a] = com
            movedc = True
        elif map[0][a] == map[2][a] == player and map[1][a] == " ":
            map[1][a] = com
            movedc = True

    if movedc == False:
        if map[0][0] == map[1][1] == player and map[2][2] == " ":
            map[2][2] = com
            movedc = True
        elif map[1][1] == map[2][2] == player and map[0][0] == " ":
            map[0][0] = com
            movedc = True
        elif map[2][2] == map[0][0] == player and map[1][1] == " ":
            map[1][1] = com
            movedc = True
        elif map[2][0] == map[1][1] == player and map[0][2] == " ":
            map[0][2] = com
            movedc = True
        elif map[1][1] == map[0][2] == player and map[2][0] == " ":
            map[2][0] = com
            movedc = True
        elif map[0][2] == map[2][0] == player and map[1][1] == " ":
            map[1][1] = com
            movedc = True

    #3. If none of the player is winning in the next move, the computer will try to apply the below strategy to create a fork

    if movedc == False:

        # Situation 1 - Computer starts first with an empty Board

        if map == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]:
            corner = random.choice(corners)
            Y1 = corner/3
            X1 = corner%3
            if X1 != 0:
                X1 -=1
            else:
                X1 = 2
                Y1 -=1
            map[Y1][X1] = com
            movedc = True

        elif map[1][1] == player:

            # Situation 2 - Opponent chose centre cell and other 8 spots are empty, then com chooses any corner

            if map[0].count(" ") == 3 and map[2].count(" ") == 3 and map[1][0] == " " and map[1][2] == " ":
                corner = random.choice(corners)                                # added a random element just to increase variety and unpredictability
                Y1 = corner/3
                X1 = corner%3
                if X1 != 0:
                    X1 -=1
                else:
                    X1 = 2
                    Y1 -=1
                map[Y1][X1] = com
                movedc = True

            # Situation 3 - When the opponent has occupied centre and last place of com was any of the corners(others cells empty)

            elif map[0][0] == com and map[2].count(" ") == 3 and map[1][0] == map[1][2] == map[0][1] == map[0][2] == " ":
                map[2][2] = com
                movedc = True
            elif map[0][2] == com and map[2].count(" ") == 3 and map[1][0] == map[1][2] == map[0][0] == map[0][1] == " ":
                map[2][0] = com
                movedc = True
            elif map[2][0] == com and map[0].count(" ") == 3 and map[1][0] == map[1][2] == map[2][1] == map[2][2] == " ":
                map[0][2] = com
                movedc = True
            elif map[2][2] == com and map[0].count(" ") == 3 and map[1][0] == map[1][2] == map[2][0] == map[2][1] == " ":
                map[0][0] = com
                movedc = True

            # Situation 4 - When the opponent has occupied centre and com has occupied any two opposite corners(other cells empty), then try a fork

            elif map[0][0] == map[2][2] == com:
                if map[0][1] == map[1][2] == " ":
                    map[0][2] = com
                    movedc = True
                elif map[1][0] == map [2][1] == " ":
                    map[2][0] = com
                    movedc = True
            elif map[0][2] == map[2][0] == com:
                if map[2][1] == map[1][2] == " ":
                    map[2][2] = com
                    movedc = True
                elif map[1][0] == map [0][1] == " ":
                    map[0][0] = com
                    movedc = True

    if movedc == False:

        # Situation 5 - When the opponent has taken the centre and all other cells are empty, then take the opposite corner

        if map[0][0] == player and map[1].count(" ") == map[2].count(" ") == 3 and map[0][1] == map[0][2] == " ":
            map[2][2] = com
            movedc = True
        elif map[0][2] == player and map[1].count(" ") == map[2].count(" ") == 3 and map[0][0] == map[0][1] == " ":
            map[2][0] = com
            movedc = True
        elif map[2][2] == player and map[0].count(" ") == map[1].count(" ") == 3 and map[2][0] == map[2][1] == " ":
            map[0][0] = com
            movedc = True
        elif map[2][0] == player and map[0].count(" ") == map[1].count(" ") == 3 and map[2][1] == map[2][2] == " ":
            map[0][2] = com
            movedc = True

        # Situations other than the above - Just try for centre, then corners and then sides if available.

        elif map[1][1] == " ":
            map[1][1] = com
            movedc = True

        while movedc == False and len(corners) > 0:
            corner = random.choice(corners)
            Y1 = corner/3
            X1 = corner%3
            if X1 != 0:
                X1 -=1
            else:
                X1 = 2
                Y1 -=1
            if map[Y1][X1] == " ":
                map[Y1][X1] = com
                movedc = True
            else:
                del corners[corners.index(corner)]                             # Delete the corner from the list if it is already taken

        while movedc == False and len(sides) > 0:
            side = random.choice(sides)
            Y1 = side/3
            X1 = side%3
            if X1 != 0:
                X1 -=1
            else:
                X1 = 2
                Y1 -=1
            if map[Y1][X1] == " ":
                map[Y1][X1] = com
                movedc = True
            else:
                del sides[sides.index(side)]                                   # Delete the side from the list if it is already taken

#We ask the player to pick either X or O and assign the other for computer. If the player inputs anything other than X or O, he/she will be asked repeatedly until he/she enters the correct value.

picked = False                                                                 # This will indicate whether the player has picked yet or not
while picked != True:
    player = raw_input("Please select what you want to use, X or O..? ")
    if player == "X" or player == "x":
        picked = True
        com = "O"
        player = "X"
    elif player == "O" or player == "o":
        picked = True
        com = "X"
        player = "O"
    else:
        print "That is a wrong input. "
        print

print
print "Great... So you are '" + player + "' and I am '" + com + "'. Let's begin the game."
print

#Here we initialize the required variables

map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False
flag = "z"                                                                     # A flag to indicate whether the move was from com or player.. z is a random value

# Any one of the below expressions are used by the computer after player choses a move

exp = ["Nice move...", "You are good.. ", "Ok... Let us see what I can do", "Hmmm... cool..", "Ok...", "You can do better than that..", "What shall I do next..!!!", "You are good.. :)", ".......", "You should not have done that..", ":(", "Duh... let me win please..", ":O", ";)", "Did you realize yet that I am going to win this game.."]

if com == "X":                                                                 # Added by vpalakur - whole if block
    make_move()
    print "As I am 'X', I will make the first move..."
    print
    print "Let me think"
    print
    time.sleep(2)

#The below loop continues till the game is complete

while done != True:
    print_board()
    print "\nOk.. your turn...\n"

    moved = False
    while moved != True:
        print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
        print "7|8|9"
        print "4|5|6"
        print "1|2|3"
        print

        try:
            pos = input("Select: ")
            print
            if pos <=9 and pos >=1:
                Y = pos/3
                X = pos%3
                if X != 0:
                    X -=1
                else:
                     X = 2
                     Y -=1

                if map[Y][X] == " ":
                    map[Y][X] = player
                    moved = True
                    flag = "p"
                    done = check_done()

                    if done == False:
                        print_board()
                        print
                        print random.choice(exp)
                        print "Let me think.."
                        print
                        time.sleep(2)
                        make_move()
                        flag = "c"
                        done = check_done()

                #Let the user know that he chose a place that was already taken

                else:
                    print "The position you have entered is already used. Please select another."        # Added by vpalakur
                    print
            
        except:
            print "You need to input a numeric value"
            print
        