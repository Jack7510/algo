#!/usr/bin/python3

'''
//
// algo for eight queens problem with recursive.
// auth: Jack 
// date: July 12, 2022
//
'''

'''
Solve eight queens problem with recursive
'''

import sys


'''
    print 8 queens in matrix
'''
def print_matrix( m ):
    for x in range(len(m)) :
        print(m[x])
    print('----------------')


def check_matrix( m ):
    for x in range(len(m)) :
        sum = 0
        for i in range(8):
            sum += m[x][i]

        if sum > 1 : 
            print('----------------')


'''
check_8_queen(matrix, row, col, i)
check_8_queen correct or not?
'''
def check_8_queen(matrix, row, col, i):
    # check the col have queen ?
    for x in range(0, row) :
        if matrix[x][i] == 1 :
            return False
    
    # check left & up
    x = row - 1
    y = i - 1
    while x >= 0 and y >= 0 :
        if matrix[x][y] == 1 :
            return False
        else:
            x -= 1
            y -= 1

    # check right & up
    x = row - 1
    y = i + 1
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
def do_8_queen(matrix, row, col):

    # row is simple, just move from col = 0 to 7
    if row == 0 :
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

            ''' 
            the row is new, shape row from 0 ~ (row - 1)
            if the lower matrix would not reshape, it is end
            '''
            if matrix[row][8] == -1 : # this row is new
                if do_8_queen(matrix, row - 1, col) != True :
                    return False
                    
            # 选择一个合适的位置放queen
            i = matrix[row][8] + 1  # begin from the last time
            while i <= 7:
                if check_8_queen(matrix, row, col, i) == True :
                    if matrix[row][8] >= 0 :
                        matrix[row][matrix[row][8]] = 0     # clear the previous 1
                    matrix[row][8] = i          # mark the position
                    matrix[row][i] = 1
                    
                    #print_matrix(matrix)
                    #check_matrix( matrix )

                    return True
                
                else: i += 1  # if i does not fit, next one
            
            # 没找到合适的位置，表示row - 1 要重新排列
            matrix[row][matrix[row][8]] = 0     # clear the previous 1
            matrix[row][8] = -1
        
    return False


'''
matrix store 8-queen info
'''
g_matrix = [
    [ 0, 0, 0, 0, 0, 0, 0, 0,-1],  # line 1
    [ 0, 0, 0, 0, 0, 0, 0, 0,-1],  # line 2
    [ 0, 0, 0, 0, 0, 0, 0, 0,-1],  # line 3
    [ 0, 0, 0, 0, 0, 0, 0, 0,-1],  # line 4
    [ 0, 0, 0, 0, 0, 0, 0, 0,-1],  # line 5
    [ 0, 0, 0, 0, 0, 0, 0, 0,-1],  # line 6
    [ 0, 0, 0, 0, 0, 0, 0, 0,-1],  # line 7
    [ 0, 0, 0, 0, 0, 0, 0, 0,-1],  # line 8
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
        