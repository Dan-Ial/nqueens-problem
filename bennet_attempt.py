import random

def get_conflicts(board, col_val, row_val):
    total_conflicts = 0
    for mem in range(len(board)):
        if mem is not col_val:
            if board[mem] == row_val and mem is not col_val:
                total_conflicts += 1
                print(col_val, ", ", row_val, " conflicts with ", mem, ", ", board[mem])
            elif abs(mem-col_val) == abs(board[mem] - row_val) and mem is not col_val:
                total_conflicts += 1
                print(col_val, ", ", row_val, " conflicts with ", mem, ", ", board[mem])

    return total_conflicts

def main():
    board = [0, 274, 236, 53, 36, 116, 21, 86, 82, 3, 165, 247, 133, 2, 45, 196, 55, 285, 169, 298, 272, 170, 262, 72, 240, 231, 17, 89, 56, 190, 204, 163, 276, 90, 254, 180, 200, 110, 280, 125, 222, 271, 47, 64, 233, 242, 269, 22, 166, 120, 16, 11, 30, 105, 189, 226, 42, 91, 164, 81, 182, 80, 106, 96, 159, 107, 37, 288, 183, 85, 97, 129, 219, 93, 139, 115, 52, 213, 257, 235, 173, 104, 151, 35, 148, 296, 124, 26, 286, 220, 137, 181, 43, 256, 232, 229, 199, 12, 241, 251, 287, 281, 177, 289, 94, 218, 161, 29, 38, 117, 145, 234, 252, 58, 121, 40, 54, 15, 1, 261, 295, 76, 221, 65, 284, 253, 70, 195, 294, 192, 71, 25, 208, 95, 140, 69, 290, 83, 74, 224, 277, 113, 7, 209, 8, 228, 216, 146, 237, 275, 147, 32, 57, 46, 156, 263, 283, 23, 230, 279, 109, 84, 286, 103, 178, 9, 246, 227, 152, 273, 6, 258, 297, 264, 51, 144, 31, 18, 292, 14, 4, 217, 119, 100, 172, 142, 270, 299, 153, 59, 143, 186, 79, 260, 203, 99, 28, 132, 87, 210, 282, 182, 123, 162, 197, 153, 160, 168, 98, 194, 291, 50, 255, 223, 33, 63, 293, 150, 118, 249, 238, 149, 268, 166, 211, 5, 135, 225, 202, 176, 68, 34, 112, 19, 48, 155, 24, 62, 66, 206, 111, 267, 174, 27, 102, 157, 108, 259, 198, 10, 136, 214, 127, 278, 167, 13, 49, 77, 114, 44, 184, 171, 266, 37, 159, 126, 154, 193, 248, 265, 130, 60, 245, 158, 175, 239, 179, 39, 279, 131, 191, 78, 201, 212, 141, 187, 67, 243, 88, 122, 172, 207, 250, 185, 101, 101, 138, 215, 205, 128]

    for i in range(300):
        print(get_conflicts(board, i, board[i]))

if __name__ == '__main__':
    main()