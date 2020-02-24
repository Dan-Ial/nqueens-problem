import random
import timeit


def create_board(size):
    """
    function that creates a board of the input size, tries to create the board to reduce number of conflicts
    :param size: size of the board
    :return: a 1D board where the index # represents the column value, and the actual number represents the row val
    """
    board = [0]
    for queen in range(1, size):
        append_vals = get_position(board, queen, size)
        board.append(append_vals)
    return board, peep_conflicts(board)

def get_position(board, col_val, size):
    position_conflicts = {}
    for row_val in range(size):
        position_conflicts[row_val] = get_conflicts(board, col_val,  row_val)
    ret_vals = min_values(position_conflicts)
    return random.choice(ret_vals)

def get_conflicts(board, col_val, row_val):
    total_conflicts = 0
    for mem in range(len(board)):
        if board[mem] == row_val and mem is not col_val:
            total_conflicts += 1
        elif abs(mem-col_val) == abs(board[mem] - row_val) and mem is not col_val:
            total_conflicts += 1
    return total_conflicts


def peep_conflicts(board):
    total = []
    for i in range(len(board)):
        total.append(get_conflicts(board, i, board[i]))
    return total


def min_values(dicti):
    min_v = min(dicti.values())
    return [pos for pos in dicti if dicti[pos] == min_v]


def check_conflicts(conflicts):
    for val in conflicts:
        if val > 0:
            return True
    return False


def min_conflicts(board, conflicts):
    max_steps = 300
    for step in range(max_steps):
        if not check_conflicts(conflicts):
            print("Solution\nSteps:", step)
            print(board)
            return True
        else:
            conflict_index = {}
            for vals in range(len(conflicts)):
                if conflicts[vals] > 0:
                    # conflict_index[column_val] = row_val
                    conflict_index[vals] = board[vals]
            val = random.choice(list(conflict_index.items()))
            ret = get_position(board, val[0], len(board))
            board[val[0]] = ret
            conflicts = peep_conflicts(board)
            # recreate everything if it reachex max
    print(board)
    return False


def main():
    random.seed(None)
    solved = False
    while not solved:
        print("restarted")
        repair = create_board(300)
        if min_conflicts(repair[0], repair[1]):
            solved = True


print(timeit.timeit(main, number=1))

#if __name__ == '__main__':
#   main()

##todo - ds for diags -> data structure which held the
# array of diagonas - each diagonal was an array and that had a column of every queen on that diagonal
## add one to all the boards for 1 indexing
# 30 arrays for 8x8 that are stored in 2 arrays of right and left

#explore having a dictionary where every queen has all rows/columns/diags stored as v
# and you can just compare vals that way - makes it O(n) instead of O(n^2)
