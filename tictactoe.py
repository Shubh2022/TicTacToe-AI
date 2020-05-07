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
    count = 0
    for i in board:
        for j in i:
            if j is not None:
                count += 1
    if count % 2 == 0:
        
        return X
    else:
        
        return O
    

   


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_moves.append((i,j))
    return set(possible_moves)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
   
    new_board = copy.deepcopy(board)
   
    if player(board) is X:
        new_board[action[0]][action[1]] = X
    elif player(board) is O:
        new_board[action[0]][action[1]] = O
    print(new_board)
    return new_board
    


    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #check rows 
    for i in board:
        if i.count(X) == 3:
            return X
        if i.count(O) == 3:
            return O
    #check columns
    for i in range(3):
        xcol = 0
        ocol = 0
        for j in range(3):
            if board[j][i] ==X:
                xcol += 1
            if board[j][i] ==O:
                ocol += 1
            if xcol == 3:
                return X
            if ocol == 3:
                return O
    #check diagonal
    #Top left to bottom right
    xdi = 0
    odi = 0
    for i in range(3):
        if board[i][i] == X:
            xdi +=1
        if xdi == 3:
            return X
        if board[i][i] == O:
            odi +=1
        if odi == 3:
            return O
    #Top right to bottom left
    xdi = 0
    odi = 0
    for i in range(3):
        if board[i][-i-1] == X:
              xdi +=1
        if xdi == 3:
            return X
        if board[i][-i-1] == O:
            odi +=1
        if odi == 3:
            return O
    return None
        




    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for i in board:
        for j in i:
            if j == None:
                return False
    return True

    
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimize(board):
    #returns the minimum value of a state

    if terminal(board):
        return utility(board)

    noa = actions(board)
    v = 9999
    for i in noa:
        v = min(v,maximize(result(board,i)))
    return v


def maximize(board):

    if terminal(board):
        return utility(board)

    noa = actions(board)
    v = -9999
    for i in noa:
        v = max(v,minimize(result(board,i)))
    return v

    
def minimax(board):
    """
    Returns the optimal action for the current player on the board
    """
    if terminal(board):
        return None
    noa = actions(board) # set


    if player(board) == X:# X is maximizing player
        v = - 9999
        for i in noa:
            v = max(v,minimize(result(board,i)))
            if v == 1:
                return i
            elif v == 0:
                return i

    if player(board) == O:# X is maximizing player
        v =  9999
        for j in noa:
            v = min(v,maximize(result(board,j)))
            if v == -1:
                return j
            elif v == 0:
                return j

    
    
