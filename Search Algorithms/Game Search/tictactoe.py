"""
Tic Tac Toe Player
"""

import math
import copy 
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
    x=0
    o=0
    for item in board:
        x=x+item.count(X)
        o=o+item.count(O)
    if x==o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions=set()
    for row,item in enumerate(board):
        for col,move in enumerate(item):
            if move==None:
                act=(row,col)
                possible_actions.add(act)
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if action not in actions(board):
        raise Exception("Invalid action")
    
    row,col=action
    board_copy=copy.deepcopy(board)

    board_copy[row][col]=player(board)
    return board_copy


def checkRow(board,player):
    for item in board:
        if item[0]==player and item[1]==player and item[2]==player:
            return True
    return False

def checkColumn(board,player):
    for col in range(len(board)):
        if board[0][col]== player and board[1][col]== player and board[2][col]==player:
            return True
    return False

def checkDiagonal(board,player):
    
    firstDiag= board[0][0]==player and board[1][1]== player and board[2][2]==player
    secDiag=board[0][2]==player and board[1][1]==player and board[2][0]==player

    return firstDiag | secDiag

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board,X) or checkColumn(board,X) or checkDiagonal(board,X):
        return X
    elif checkRow(board,O) or checkColumn(board,O) or checkDiagonal(board,O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not EMPTY:
        return True
    
    for item in board:
        if EMPTY in item:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X: 
        return 1
    elif winner(board)==O:
        return -1
    else: 
        return 0

def maxValue(board):

    v = - math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v= max(v,minValue(result(board,action)))    
    return v

def minValue(board):

    v =  math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v= min(v,maxValue(result(board,action)))    
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): 
        return None
    
    elif player(board)==X:

        plays=[]
        #Loop over the possible actions
        for action in actions(board):
            #Add to plays list a tuple with the min_value and the action 
            plays.append([minValue(result(board,action)),action])
        #Reverse sort for the plays list and get the actions that should be taken
        return sorted(plays,key= lambda x:x[0],reverse=True)[0][1]

    elif player(board)==O:

        plays=[]
        #Loop over the possible actions
        for action in actions(board):
            #Add to plays list a tuple with the max_value and the action 
            plays.append([maxValue(result(board,action)),action])
        #Reverse sort for the plays list and get the actions that should be taken
        return sorted(plays,key= lambda x:x[0])[0][1]

