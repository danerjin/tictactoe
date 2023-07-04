"""
Tic Tac Toe Player
"""
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
    if terminal(board):
        return
    x = 0
    o = 0
    for i in board:
        for j in i:
            if j == X:
                x += 1
            elif j == O:
                o += 1
    if x > o:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions_set.append((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = copy.deepcopy(board)
    board2[action[0]][action[1]] = player(board2)
    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    map = ['O',None,'X']
    return map[utility(board)+1]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if None == utility(board):
        return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and not board[i][0] == EMPTY:
            if board[i][0] == O:
                return -1
            else:
                return 1
        if board[0][i] == board[1][i] == board[2][i] and not board[0][i] == EMPTY:
            if board[0][i] == O:
                return -1
            else:
                return 1
    if board[0][0] == board[1][1] == board[2][2] and not board[0][0] == EMPTY:
        if board[0][0] == O:
            return -1
        else:
            return 1
    if board[0][2] == board[1][1] == board[2][0] and not board[0][2] == EMPTY:
        if board[0][2] == O:
            return -1
        else:
            return 1
    for i in board:
        for j in i:
            if j == EMPTY:
                return None
    return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -100000000000
    for action in actions(board):
        v = max(v,min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 100000000000
    for action in actions(board):
        v = min(v,max_value(result(board, action)))
    return v


def max_action(board):
    if terminal(board):
        return None
    v = -100000000000
    best_action = None
    for action in actions(board):
        if min_value(result(board, action)) >= v:
            best_action = action
        v = max(v,min_value(result(board, action)))
    return best_action


def min_action(board2):
    if terminal(board2):
        return None
    v = 100000000000
    best_action = None
    for action in actions(board2):
        if max_value(result(board2, action)) <= v:
            best_action = action
        v = min(v,max_value(result(board2, action)))
    return best_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == O:
        return min_action(board)
    else:
        return max_action(board)
