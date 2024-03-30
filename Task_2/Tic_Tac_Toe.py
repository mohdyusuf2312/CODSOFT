import random

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



def ai_move(turn, board, aiturn, corner):
    data = []


print_board(turn, board, aiturn)