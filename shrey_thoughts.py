import random
import timeit



def create_board(size):
    """
    function that creates a board of the input size, tries to create the board to reduce number of conflicts
    :param size: size of the board
    :return: a 1D board where the index # represents the column value, and the actual number represents the row val
    """
    board = [0]
    rows = {0: 1}
    diags = {0: 1}
    for col in range(1, size):
        append_vals = get_position(board, col, size, rows, diags)
        board.append(append_vals)
        rows[append_vals] = 1
        diags[col - append_vals] = 1
    return board, peep_conflicts(board, rows, diags), rows, diags


def get_position(board, col_val, size, rows, diags):
    position_conflicts = {}
    for row_val in range(size):
        position_conflicts[row_val] = get_conflicts(board, col_val,  row_val, rows, diags)
    ret_vals = min_values(position_conflicts)
    return random.choice(ret_vals)


def get_conflicts(board, col_val, row_val, rows, diags):
    total = 0
    if row_val in rows and rows[row_val] > 0:
        total += 1
    if col_val - row_val in diags and diags[col_val - row_val] > 0:
        total += 1
    return total
    # total_conflicts = 0
    # for mem in range(len(board)):
    #     if board[mem] == row_val and mem is not col_val:
    #         total_conflicts += 1
    #     elif abs(mem-col_val) == abs(board[mem] - row_val) and mem is not col_val:
    #         total_conflicts += 1
    # return total_conflicts


def peep_conflicts(board, rows, diags):
    total = []
    for i in range(len(board)):
        total.append(get_conflicts(board, i, board[i], rows, diags))
    return total


def min_values(dicti):
    min_v = min(dicti.values())
    return [pos for pos in dicti if dicti[pos] == min_v]


def check_conflicts(conflicts):
    for val in conflicts:
        if val > 0:
            return True
    return False


def min_conflicts(board, conflicts, rows, diags):
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
            ret = get_position(board, val[0], len(board), rows, diags)
            if ret in rows:
                rows[ret] += 1
            else:
                rows[ret] = 1
            rows[val[1]] -= 1
            diags[val[0] - val[1] ] -= 1
            if val[0]-ret in diags:
                diags[val[0]-ret] += 1
            else:
                diags[val[0] - ret] = 1
            board[val[0]] = ret
            conflicts = peep_conflicts(board, rows, diags)
            # recreate everything if it reachex max
    return False


def main():
    solved = False
    print(create_board(10))
    while not solved:
        print("restarted")
        repair = create_board(10)
        if min_conflicts(repair[0], repair[1], repair[2], repair[3]):
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