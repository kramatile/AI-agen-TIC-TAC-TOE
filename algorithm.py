import math
import copy
import numpy as np
def check_win(board):
    # Check rows
    if all(i == board[0][0] for i in board[0]) and 0 not in board[0]:
        return board[0][0]
    elif all(i == board[1][0] for i in board[1])and 0 not in board[1]:
        return board[1][0]
    elif all(i == board[2][0] for i in board[2])and 0 not in board[2]:
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != 0:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != 0:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != 0:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0 :
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    else:
        return None

def check_terminal(board):
    if(check_win(board) != None):
        return True
    else: 
        for i in range(3):
            if 0 in board[i]:
                return False
        return True
    
def get_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def utility(board):
    if check_win(board) == 1:
        return 1
    elif check_win(board) == -1:
        return -1
    else :
        return 0

import math

import math

def minimax(board, maximizing_player=True):
    if check_terminal(board):
        return utility(board), None
    
    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for move in get_moves(board):
            new_board = [row[:] for row in board]
            new_board[move[0]][move[1]] = 1
            eval, _ = minimax(new_board, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for move in get_moves(board):
            new_board = [row[:] for row in board]
            new_board[move[0]][move[1]] = -1
            eval, _ = minimax(new_board, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move
    

def minimax(board, alpha, beta, maximizing_player=True):
    if check_terminal(board):
        return utility(board), None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for move in get_moves(board):
            new_board = [row[:] for row in board]
            new_board[move[0]][move[1]] = 1
            eval, _ = minimax(new_board, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for move in get_moves(board):
            new_board = [row[:] for row in board]
            new_board[move[0]][move[1]] = -1
            eval, _ = minimax(new_board, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return min_eval, best_move


def max_value(position):
    if check_terminal(position):
        return utility(position), None

    v = -math.inf
    best_position = None
    for action in get_moves(position):
        val, _ = min_value(result(position, action, "O"))
        if val > v:
            v = val
            best_position = action
    return v, best_position

def min_value(position):
    if check_terminal(position):
        return utility(position), None

    v = math.inf
    best_position = None
    for action in get_moves(position):
        val, _ = max_value(result(position, action, "X"))
        if val < v:
            v = val
            best_position = action
    return v, best_position


def result(grid,action,player):
    grid1 = copy.deepcopy(grid)
    if player == "X":
        grid1[action[0]][action[1]] = 1
    else:
        grid1[action[0]][action[1]] = -1 
    return grid1


test_grid = [
    [1, 0, -1],
    [0, -1, 0],
    [0, 0, 1]
]

print(minimax(test_grid,-np.inf,np.inf,True)[1])