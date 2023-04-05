from random import choice

board = [1,2,3,4,5,6,7,8,9]
win_comb = [[1,2,3],[1,5,9],[1,4,7],[2,5,8],[3,6,9],[4,5,6],[7,8,9], \
                    [3,5,7],[2,5,8]]
user = []
machine = []

user_chip = str(input("Enter your chip symbol: 'X' or 'O'   "))

if user_chip !="X" and user_chip !="O":
    user_chip = str(input("Enter correct chip symbol: 'X' or 'O'   "))

if user_chip == "X":
    machine_chip = "O"
    print("Welcome To the Game!!! ", "Machine is:", machine_chip)
elif user_chip == "O":
    machine_chip = "X"
    print("Welcome To the Game!!! ", "Machine is:", machine_chip)
else:
    print ("Machine WIN!!!")



def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    user_field = 00
    free_fields = free_fields_lst(board)

    if len(free_fields)>0:
        user_field = int(input("Enter your choice from free fields:"))

    while (user_field not in free_fields) and len(free_fields)>0:
        user_field = int(input("Please, make your choice of free field!:"))

    #if type(user_field) == int:
    for i in range(len(board)):
        if board[i] == user_field:
            user.append(board[i])
            board[i] = user_chip

    return board



def free_fields_lst(board):
    print("Free Fields")
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in board:
        if i != "X" and i !="O":
            free_fields.append(i)
            
    print(free_fields)
    return free_fields


def draw_move(board):

    # The function draws the computer's move and updates the board.
    machine_field = 00
    free_fields = free_fields_lst(board)
    if len(free_fields) > 0:
        for e in range(len(win_comb)):
                comb = 0
                for j in win_comb[e]:
                    for p in range(len(free_fields)):
                        if j == free_fields[p]:
                            comb +=1
                            if comb == len(win_comb[e]):
                                machine_field = choice(win_comb[e])
                                machine.append(machine_field)
                            else:
                                machine_field = choice(free_fields)
                                machine.append(machine_field)
                            for i in range(len(board)):
                                    if board[i] == machine_field:
                                        board[i] = machine_chip
                                        return board

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print("+------","+------+","------+", sep="")
    print("|      ","|      |","      |", sep="")
    print("|  ",board[0],"   ","|  ",board[1],"   |","   ",board[2],"  |", sep="")
    print("|      ","|      |","      |", sep="")
    print("+------","+------+","------+", sep="")
    print("|      ","|      |","      |", sep="")
    print("|  ",board[3],"   ","|  ",board[4],"   |","   ",board[5],"  |", sep="")
    print("|      ","|      |","      |", sep="")
    print("+------","+------+","------+", sep="")
    print("|      ","|      |","      |", sep="")
    print("|  ",board[6],"   ","|  ",board[7],"   |","   ",board[8],"  |", sep="")
    print("|      ","|      |","      |", sep="")
    print("+------","+------+","------+", sep="")


def victory_for(user=[], machine=[]):
    # print("Victory is for!")
    # The function analyzes the board's status - througth win combinations list
    #  in order to check if the player using 'O's or 'X's has won the game
    winner = ''
    user_winner, machine_winner = 0, 0

    for n in range(len(win_comb)):
        #print(n)
        user_win = 0
        machine_win = 0
        for m in win_comb[n]:
            #print(m)
            for l in user:
                if m == l:
                    user_win += 1
                if user_win == 3: user_winner = 1
                #print(user_win)
            for l in machine:
                if m == l:
                    machine_win += 1
                if machine_win == 3: machine_winner = 1
                #print(machine_win)
    
    if user_winner > machine_winner:
        winner = user_chip + "  You Won!!!"
        return winner
    elif user_winner < machine_winner:
        winner = machine_chip + "  Machine Won!!!"
        return winner
    else:
        winner = ''
        return winner
    




flag = True
k = 0

display_board(board)

while flag:
    board = enter_move(board)
    display_board(board)

    if victory_for(user, machine):
        flag = False
        print(victory_for(user, machine))
        break

    board = draw_move(board)
    display_board(board)

    if victory_for(user, machine):
        flag = False
        print(victory_for(user, machine))
        break
    
    k += 1

    if k == 5: 
        flag = False
        print("No Winner - it's draw!!")
        break
    
    
    
    
