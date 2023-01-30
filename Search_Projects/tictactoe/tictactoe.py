"""
Tic Tac Toe Player
"""
from math import inf
import math
from copy import deepcopy
from random import choice
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    O_num = 0
    X_num = 0
    
    for element in board:
        for e in element:
            if e == O:
                O_num += 1
            elif e == X:
                X_num += 1
    if O_num == X_num:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_list.append((i, j))

    return action_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    boards_list = []
    if player(board) == X:
        board_copy = deepcopy(board)
        board_copy[action[0]][action[1]] = X
        board_option = board_copy[:]
        boards_list += board_option
    else:
        board_copy = deepcopy(board)
        board_copy[action[0]][action[1]] = O
        board_option = board_copy[:]
        boards_list += board_option
    
    return  boards_list  


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
        for element in board:
            for e in element:
                if e == EMPTY:
                    return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1 
        else:
            return 0
    return 0


def maxvalue(board):
    if terminal(board) == True:
        return utility(board)
    v = -inf
    for a in actions(board):
        v = max(v, minvalue(result(board, a)))
    return v

def minvalue(board):
    if terminal(board) == True:
        return utility(board)
    v = inf
    for a in actions(board):
        v = min(v, maxvalue(result(board, a)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    n = 0
    
    for i in board:
        for j in i:
            if j == EMPTY:
                n += 1
            
    if n == 9:
        return (1, 1)
    
    else:
        if player(board) == X:
            previous_score = -inf
            for a in actions(board):
                score = minvalue(result(board, a))
                if score > previous_score:
                    previous_score = score
                    action_to_take = a
            return action_to_take    
    
        
        if player(board) == O:
            previous_score = inf
            for a in actions(board):
                score = maxvalue(result(board, a))
                if score < previous_score:
                    previous_score = score
                    action_to_take = a
            return action_to_take 