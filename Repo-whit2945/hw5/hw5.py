import random
#==========================================
# Purpose: The function determines if there are any students
# that are wizards by tracking students' grades, social lives, and sleep.
# If their name appears in all three categories (indicating that they are excelling
# in all three categories) then they are a wizard. 
# Input Parameter(s): The three input parameters are: grades, life and sleep.
# These variables represent a good quality of grades, social life or sleep if a student
# 's name appears in those categories.
# Return Value(s): returns a list of students that are wizards; students
# that have their names in all three categories.
#==========================================

def wizards(grades, life, sleep):
    num = len(grades) + len(life) + len(sleep)
    wizlist = [""]*num
    count = 0
    for i in range(len(grades)):
        for j in range(len(life)):
            for s in range(len(sleep)):
                if (grades[i] == life[j]) and (sleep[s] == grades[i]) and (life[j] == sleep[s]):
                    wizlist[count] = grades[i]
                    count+=1
    return wizlist[0:count]

#==========================================
# Purpose: This function returns the number of slots containing '-' at their indexes
# Input Parameter(s): A list titled 'board'. This list should only contain 9
# elements; ranges 0-8
# Return Value(s): returns list of the numbered slots that have the value '-'
# indicating that they are empty. 
#==========================================

def open_slots(board):
    count = 0
    boardD = [''] *9
    for i in range(9):
        if board[i] == '-':
            boardD[count] = i 
            count+=1
    return boardD[0:count]
            
#==========================================
# Purpose: This function takes a list of elements; 'X', 'O', or '-'.
# and determines if 'X' wins, 'O' wins, 'D' for draw, or if '-' 
# symbolizes that the game is on going. 
# Input Parameter(s): A list titled 'board'. This list should only contain 9
# elements; ranges 0-8. Containing 'X','O', or '-'
# Return Value(s): Accourding to a series of if statements either an 'X','O'
# 'D' or '-'. Showing a winner, a draw, or that the game isn't finished. 
#==========================================
def winner(board):
    if ((board[0] == 'X') and (board[1] == 'X') and (board[2] == 'X')) or ((board[3] == 'X') and (board[4] == 'X') and (board[5] == 'X')):
        return 'X'
    elif ((board[6] == 'X') and (board[7] == 'X') and (board[8] == 'X')) or ((board[0] == 'X') and (board[3] == 'X') and (board[6] == 'X')):
        return 'X'
    elif ((board[1] == 'X') and (board[4] == 'X') and (board[7] == 'X')) or ((board[2] == 'X') and (board[5] == 'X') and (board[8] == 'X')):
        return 'X'
    elif ((board[0] == 'X') and (board[4] == 'X') and (board[8] == 'X')) or ((board[2] == 'X') and (board[4] == 'X') and (board[6] == 'X')):
        return 'X'
    elif ((board[0] == 'O') and (board[1] == 'O') and (board[2] == 'O')) or ((board[3] == 'O') and (board[4] == 'O') and (board[5] == 'O')):
        return 'O'
    elif ((board[6] == 'O') and (board[7] == 'O') and (board[8] == 'O')) or ((board[0] == 'O') and (board[3] == 'O') and (board[6] == 'O')):
        return 'O'
    elif ((board[1] == 'O') and (board[4] == 'O') and (board[7] == 'O')) or ((board[2] == 'O') and (board[5] == 'O') and (board[8] == 'O')):
        return 'O'
    elif ((board[0] == 'O') and (board[4] == 'O') and (board[8] == 'O')) or ((board[2] == 'O') and (board[4] == 'O') and (board[6] == 'O')):
        return 'O'
    elif open_slots(board) == []:
        return 'D'
    else:
        return '-'
    
#==========================================
# Purpose: This fuction plays a game of tic tac toe
# by filling up a list with 'X's and 'O's in random places.
# Then it sends the list to the 'winner' function to determine the winner
# or if there's a draw. 
# Input Parameter(s): This function has no input parameters
# Return Value(s): A call to the 'winner' function with the board list
# gets returned. That usually gets evaluated to either 'X', 'O' or 'D'.
#==========================================        
def tic_tac_toe():
    board = ['-','-','-']*3
    b = r_list()
    for i in range(9):
        if(i%2 == 0):
           board[b[i]] = 'X'
        if(i%2 != 0):
          board[b[i]] = 'O'
    return winner(board)

#==========================================
# Purpose: The purpose of this function is to generate
# a list of 9 random numbers. These numbers are 0-8
# and no one number repeats.
# Input Parameter(s): There are no input parameters.
# Return Value(s): This function returns list 'll' 
#========================================== 
def r_list():
    ll = [0]*9
    zero_c = 0
    one_c = 0
    two_c = 0
    three_c = 0
    four_c = 0
    five_c = 0
    six_c = 0
    seven_c = 0
    eight_c = 0
    ran = 0
    count = 0
    for i in range(1000):
        ran = random.randint(0,8)
        if (ran == 0) and (zero_c == 0):
            ll[count] = ran
            zero_c += 1
            count +=1
        if (ran == 1) and (one_c == 0):
            ll[count] = ran
            one_c += 1
            count+=1
        if (ran == 2) and (two_c == 0):
            ll[count] = ran
            two_c += 1
            count+=1
        if (ran == 3) and (three_c == 0):
            ll[count] = ran
            three_c += 1
            count+=1
        if (ran == 4) and (four_c == 0):
            ll[count] = ran
            four_c += 1
            count+=1
        if (ran == 5) and (five_c == 0):
            ll[count] = ran
            five_c += 1
            count+=1
        if (ran == 6) and (six_c == 0):
            ll[count] = ran
            six_c += 1
            count+=1
        if (ran == 7) and (seven_c == 0):
            ll[count] = ran
            seven_c += 1
            count+=1
        if (ran == 8) and (eight_c == 0):
            ll[count] = ran
            eight_c += 1
            count+=1
    return ll
    
#==========================================
# Purpose: This function plays tic tac toe 'n' amount of
# times. And prints the results.
# Input Parameter(s): This function has one input
# parameter, 'n'. This input parameter decides how many
# games are played.
# Return Value(s): This function returns nothing
#==========================================
def play_games(n):
    tic = ''
    OO = 0
    XX = 0
    DD = 0
    for k in range(n):
        tic = tic_tac_toe()
        if tic == 'X':
            XX+=1
        if tic == 'O':
            OO+=1
        if tic == 'D':
            DD+=1
    print("X wins: ",XX)
    print("O wins: ", OO)
    print("Draws: ", DD)

