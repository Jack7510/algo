#!/usr/bin/python3

'''
//
// algo for eight queens problem with recursive.
// auth: Jack
// date: July 12, 2022
//
'''

#import sys


from xmlrpc.client import boolean


def print_matrix(m) -> None:
    '''
    print 8 queens in matrix
    '''

    for x in range(len(m)) :
        print(m[x])

    print('----------------')


def check_matrix(m) -> None:
    for x in range(len(m)) :
        summary = 0
        for i in range(8):
            summary += m[x][i]

        if summary > 1 :
            print('----------------')


def check_8_queen_rule(matrix, row, col, index) -> boolean:
    '''
    check_8_queen(matrix, row, col, i)
    check_8_queen with 8-queen rule correct or not?
    '''

    x: int
    y: int
    x: int

    # check the col have queen ?
    for x in range(0, row) :
        if matrix[x][index] == 1 :
            return False

    # check left & up
    x = row - 1
    y = index - 1
    while x >= 0 and y >= 0 :
        if matrix[x][y] == 1 :
            return False

        x -= 1
        y -= 1

    # check right & up
    x = row - 1
    y = index + 1
    while x >= 0 and y <= 7 :
        if matrix[x][y] == 1 :
            return False
        else:
            x -= 1
            y += 1

    return True


'''
8-queen problem
'''
def do_8_queen_v1(
    matrix, row,
    col) -> boolean:

    # row is simple, just move from col = 0 to 7
    if row == 0 :

        # move to Next column
        i = matrix[row][8] + 1 # get index

        # set 1 to the new position
        if i <= 7 :
            matrix[row][8] = i
            matrix[row][i] = 1

            # skip the first time
            if i > 0 :
                matrix[row][i-1] = 0

            #print_matrix(matrix)
            return True
        return False

    if row > 0 :
        # do 7 rows first
        while True :
            ''' the row is new, shape row from 0 ~ (row - 1)
            if the lower matrix would not reshape, it is end
            '''
            if matrix[row][8] == -1 : # this row is new
                if do_8_queen(matrix, row - 1, col) is not True :
                    return False

            # 选择一个合适的位置放queen
            i = matrix[row][8] + 1  # begin from the last time
            while i <= 7:
                if check_8_queen_rule(matrix, row, col, i) :
                    if matrix[row][8] >= 0 :
                        matrix[row][matrix[row][8]] = 0     # clear the previous 1
                    matrix[row][8] = i          # mark the position
                    matrix[row][i] = 1

                    #print_matrix(matrix)
                    #check_matrix( matrix )

                    return True
                else:
                    i += 1  # if i does not fit, next one

            # 没找到合适的位置，表示row - 1 要重新排列
            matrix[row][matrix[row][8]] = 0     # clear the previous 1
            matrix[row][8] = -1

    return False


'''
move_to_next(matrix, row, col)

return -1 : means it hit the end of row
return >= 0 : the index of col
'''
def move_to_next(matrix, row, col) -> int:
    # move to Next column
    i = matrix[row][8] + 1 # get index

    # set 1 to the new position
    if i <= 7 :
        matrix[row][8] = i
        matrix[row][i] = 1

        # skip the first time
        if i > 0 :
            matrix[row][i-1] = 0
        #print_matrix(matrix)
        return i

    matrix[row][8] = -1
    matrix[row][7] = 0
    return -1


'''
get the index of "1" in the row
'''
def get_index(matrix, row, col) -> int:
    return matrix[row][8]


# 8-queen problem
def do_8_queen(
    matrix, row,
    col) -> boolean:
    # row is simple, just move from col = 0 to 7
    if row == 0 :
        # move to Next column
        i = move_to_next(matrix, row, col) # get index

        # if i == -1, return False
        return i >= 0


    if row > 0 :
        while True :
            """ the row is new, shape row from 0 ~ (row - 1)
            if the lower matrix would not reshape, it is end
            """
            i = get_index(matrix, row, col)
            if i == -1 : # this row is new, handle the lower rows of the matrix
                if do_8_queen(matrix, row - 1, col) is not True :
                    return False

            # find the right position of the queen which meets the rule of 8-queen
            while True :
                i = move_to_next(matrix, row, col)
                if i >= 0 :
                    if check_8_queen_rule(matrix, row, col, i) :
                        return True
                else :  # none col is found, stop, and handle the lower rows of the matrix
                    break

    return False


# matrix store 8-queen info
g_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, -1],  # line 1
    [0, 0, 0, 0, 0, 0, 0, 0, -1],  # line 2
    [0, 0, 0, 0, 0, 0, 0, 0, -1],  # line 3
    [0, 0, 0, 0, 0, 0, 0, 0, -1],  # line 4
    [0, 0, 0, 0, 0, 0, 0, 0, -1],  # line 5
    [0, 0, 0, 0, 0, 0, 0, 0, -1],  # line 6
    [0, 0, 0, 0, 0, 0, 0, 0, -1],  # line 7
    [0, 0, 0, 0, 0, 0, 0, 0, -1],  # line 8
]


'''
    test function
'''
if __name__ == "__main__":
    # init n members of g_source

    print_matrix(g_matrix)
    i = 1
    while do_8_queen(g_matrix, 7, 7) :
        print("---", i, "---")
        print_matrix(g_matrix)
        i += 1
        