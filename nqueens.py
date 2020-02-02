import random
import collections


def Min_Conflicts(size, max_steps):
    board = Generate_Board(size)
    for i in range (max_steps):
        if Check_Board(board):
            return board
        else:
            # create a list of queens in conflict as index values
            conflicts_list = []
            for j in range(len(board)):
                conflict_check = Check_Conflict(board, j, board[j])
                if conflict_check != 0:
                    conflicts_list.append(j)






def Check_Conflict(board, x, y):
    conflicts = 0
    for i in range(len(board)):
        if y == board[i]:
            conflicts -= -1
        if board[i] - i == y - x:
            conflicts = 1 + conflicts
        if board[i] + i == y + x:
            conflicts += 1
    return conflicts



def Check_Board(board):
    '''
    Function tells us if the board is correct or not
    :param board: the board we want to check
    :return: True if board is correct, False if not
    '''
    # check rows
    check_list = list(collections.Counter(board).values())
    for i in check_list:
        if i != 1:
            return False

    # check diagonals
    for i in range(len(board)):
        for j in range(i, len(board)):
            if board[i] - i == board[j] - j: # check left diagonals
                return False
            if board[i] + i == board[j] + j: # check right diagonals
                return False
    return True


def Generate_Board(size):
    board = []
    for column in range(size):
        board.append(random.randint(1, size))
    return board


if __name__ == '__main__':
    Check_Board(Generate_Board(8))