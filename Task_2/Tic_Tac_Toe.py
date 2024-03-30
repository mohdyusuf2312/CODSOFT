import random
from logo import logo

print(logo)
print("Welcome to the unbeatable Tic Tac Toe")
print("The board's index values are: ")
print("0|1|2")
print("3|4|5")
print("6|7|8")
print("Enter your move, 0 through 8. (You are X's and AI is O's) ")

board = ["_","_","_","_","_","_"," "," "," "] #Board horizontal lines
pairs = ([0,3,6],[1,4,7],[2,4,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]) #Win Pairs
corner = [0,2,6,8] #corner of the board

turn = "PLAYER"

aiturn = 0 #number of turn of ai

def print_board(turn, board, aiturn):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("Turn :" + str(turn))
    if turn == 0: #For first move
        player_move(turn, board, aiturn)
    if turn == "AI": #if ai_move
        aiturn += 1
        ai_move(turn, board, aiturn, corner)
    if turn == "PLAYER": #if player_move
        player_move(turn, board, aiturn)

def player_move(turn, board, aiturn):
    choice = input("Enter your move (0-8): ")
    board[int(choice)] = "X" # update board when player's move have done.
    turn = "AI" # change turn to AI, now its ai_move
    check_win(turn, board, aiturn)

def check_win(turn, board, aiturn):
    for n in pairs:
        first = board[n[0]]
        second = board[n[1]]
        third = board[n[2]]
        if first == second and second == third:
            if first == "O":
                print("You lose! AI win")
            if first == "X": # This instruction will never run because this program is write for unbeatable Tic Tac Toe
                print("You win!")
        else:
            filled_space =0
            for x in range(8):
                if board[x] != " " and board[x] != "_":
                    filled_space +=1
                if filled_space == 8:
                    print("It's draw! You can't win.")

    print_board(turn, board, aiturn)

def ai_move(turn, board, aiturn, corner):
    already_moved = False

    def corner_choice(corner, board, already_moved):
        best_choices = []
        if not already_moved:
            for n in corner:
                if board[n] == " " or board[n] == "_":
                    best_choices.append(n)
            board[random.choice(best_choices)] = "O"

    if aiturn == 1:
        if board[4] != "X": #to check whether that middle space is already moved by the player or not if not that taken by the ai, or if taken by the player then ai have to move corner move
            board[4] == "O" #Middle move by ai
            already_moved = True
        else:
            corner_choice(corner, board, already_moved)
            already_moved = True
    check_win(turn, board, aiturn)

print_board(turn, board, aiturn)