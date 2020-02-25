import random


def create_board(size):
    """
    function that creates a board of the input size, tries to create the board to reduce number of conflicts
    :param size: size of the board
    :return: a 1D board where the index # represents the column value, and the actual number represents the row val
    """
    board = []
    rows = {}
    for i in range(size):
        rows[i] = 0
    ldiags = {}
    for i in range(-(size - 1), size):
         ldiags[i] = 0
    rdiags = {}
    for i in range(0, 2 * size - 1):
        rdiags[i] = 0

    i = 0
    col = 0
    while i < size:
        board.append(i)
        rows[i] += 1
        ldiags[i-col] += 1
        rdiags[i+col] += 1
        i += 2
        col += 1
    i = 1
    while i < size:
        board.append(i)
        rows[i] += 1
        ldiags[i - col] += 1
        rdiags[i + col] += 1
        col += 1
        i += 2
    return board, peep_conflicts(board, rows, ldiags, rdiags), rows, ldiags, rdiags


def generate_position(board, col_val, size, rows, ldiags, rdiags):
    position_conflicts = {}
    for row_val in range(size):
        position_conflicts[row_val] = get_conflicts(board, col_val,  row_val, rows, ldiags, rdiags)
    ret_vals = min_values(position_conflicts)
    result = random.choice(ret_vals)

    rows[result] += 1
    ldiags[result - col_val] += 1
    rdiags[result + col_val] += 1

    return result, rows, ldiags, rdiags


def get_position(board, col_val, size, rows, ldiags, rdiags):
    position_conflicts = {}
    for row_val in range(size):
        position_conflicts[row_val] = get_conflicts(board, col_val,  row_val, rows, ldiags, rdiags)
    ret_vals = min_values(position_conflicts)

    if position_conflicts[ret_vals[0]] > position_conflicts[board[col_val]]:
        return board[col_val], rows, ldiags, rdiags
    else:
        result = random.choice(ret_vals)
        rows[board[col_val]] -= 1
        ldiags[board[col_val] - col_val] -= 1
        rdiags[board[col_val] + col_val] -= 1

        rows[result] += 1
        ldiags[result - col_val] += 1
        rdiags[col_val + result] += 1
        return result, rows, ldiags, rdiags


def get_conflicts(board, col_val, row_val, rows, ldiags, rdiags):
    total_conflicts = 0
    if rows[row_val] >= 1:
        if row_val == board[col_val]:
            total_conflicts += rows[row_val] - 1
        else:
            total_conflicts += rows[row_val]
    if ldiags[row_val-col_val] >= 1:
        if row_val == board[col_val]:
            total_conflicts += ldiags[row_val-col_val] - 1
        else:
            total_conflicts += ldiags[row_val-col_val]
    if rdiags[row_val+col_val] >= 1:
        if row_val == board[col_val]:
            total_conflicts += rdiags[row_val+col_val] - 1
        else:
            total_conflicts += rdiags[row_val+col_val]

    return total_conflicts


def peep_conflicts(board, rows, ldiags, rdiags):
    total = []
    for i in range(len(board)):
        total.append(get_conflicts(board, i, board[i], rows, ldiags, rdiags))
    return total


def min_values(dicti):
    min_v = min(dicti.values())
    return [pos for pos in dicti if dicti[pos] == min_v]


def check_conflicts(conflicts):
    for val in conflicts:
        if val > 0:
            return True
    return False


def min_conflicts(board, conflicts, rows, ldiags, rdiags):
    max_steps = len(board)
    lastval = -1
    for step in range(max_steps):
        if not check_conflicts(conflicts):
            return True
        else:
            conflict_index = {}
            for vals in range(len(conflicts)):

                if conflicts[vals] > 0:
                    # conflict_index[column_val] = row_val
                    conflict_index[vals] = board[vals]

            freshval = False
            while not freshval:
                val = random.choice(list(conflict_index.items()))
                if val[0] != lastval:
                    freshval = True
                    lastval = val[0]
            ret = get_position(board, val[0], len(board), rows, ldiags, rdiags)
            board[val[0]] = ret[0]
            rows = ret[1]
            ldiags = ret[2]
            rdiags = ret[3]
            #print(board)
            conflicts = peep_conflicts(board, rows, ldiags, rdiags)
            # recreate everything if it reaches max
    return False

def run_test(sample_size):
    random.seed(None)
    solved = False
    while not solved:
        print("re")
        repair = create_board(sample_size)
        if min_conflicts(repair[0], repair[1], repair[2], repair[3], repair[4]):
            solved = True
    return repair[0]

def main():
    # file input
    with open("nqueens.txt", 'r') as f_input:
        # read nqueens.txt into a list and convert all elements to int
        file_list = [int(x) for x in f_input.readlines()]
        # only accept inputs between 3 and 10000000
        file_list = [x for x in file_list if 3 < x <= 10000000]

    # run tests for each x value
    result_list = [run_test(i) for i in file_list]

    # file output
    with open("nqueens_out.txt", 'w') as f_output:
        # convert all elements to a string and add a \n
        output_list = [str(x) + "\n" for x in result_list]
        # remove the \n from the last element
        output_list[-1] = output_list[-1][:-1]
        # write to the file
        f_output.writelines(output_list)

if __name__ == '__main__':
    main()

##todo - ds for diags -> data structure which held the
# array of diagonas - each diagonal was an array and that had a column of every queen on that diagonal
## add one to all the boards for 1 indexing
# 30 arrays for 8x8 that are stored in 2 arrays of right and left

#explore having a dictionary where every queen has all rows/columns/diags stored as v
# and you can just compare vals that way - makes it O(n) instead of O(n^2)
