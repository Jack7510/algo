'''
《计算之魂》 思考题3.6 
    如果采用本节存储稀疏矩阵的方法存储了两个矩阵，如何实现矩阵的加法运算？

Author: Jack Lee
Date:   July 30, 2022

Description:
    用按行索引并存储“非零”项，按列索引存储“非零”项。并实现两个相加。可以大量节约空间和提升速度。

History: 
July 30, 2022, version 1.0

'''

import numpy as np


class RowInfo :
    def __init__(self, col, val):
        self.col = col
        self.val = val


class ColInfo :
    def __init__(self, row, pos):
        self.row = row
        self.pos = pos


'''
build spare matrix from normal matrix
'''
class spare_matrix:
    
    def __build(self, matrix) -> None:
        # scan the whole matrix, T(n) = O(n**2)
        for i in range(0, self.m):
            for j in range(0, self.n):
                if matrix[i][j] != 0:
                    info = RowInfo(j, matrix[i][j])
                    self.row_info.append(info)

            # 下一行的开始就是当前的末尾
            if (i + 1) < self.m :
                self.row_index[i+1] = len(self.row_info)
        
        # build index of cols
        for i in range(0, self.m): # 遍历 表3.6, i 为行号
            if i == self.m - 1 :  # the last row
                last_row = len(self.row_info)
            else:
                last_row = self.row_index[i+1]
            for j in range(self.row_index[i], last_row): # 遍历一行所有的非零列
                if self.row_info[j].col >= (self.n - 1): # the last col
                    self.col_info.append(ColInfo(i, j))
                else:   # 插入下一列的前面，后面的位置都+1
                    self.col_info.insert(self.col_index[self.row_info[j].col + 1], ColInfo(i, j))
                    for k in range(self.row_info[j].col + 1, self.n):
                        self.col_index[k] += 1


    '''
    matrix - the normal matrix to handle
    m - the # of rows in matrix
    n - the # of cols in matrix
    '''
    def __init__(self, matrix=None, m=0, n=0):
        self.m = m
        self.n = n
        self.row_info = []  # 对应的非零元素的列号和数值表[列号, 元素的值]
        self.row_index = [0 for x in range(0, m)]         # 对应的每一行非零元素的起始位置 
        self.col_info = []  # 对应的非零元素的行号和元素所在row_info中的位置[行号，元素所在的位置]
        self.col_index = [0 for y in range(0, n)]         # 对应的每一列非零元素索引在col_info中的位置
        
        if matrix is not None:
            self.__build(matrix)

    # print the matrix with spare matrix info
    def print(self) -> None:
        # print matrix from row to row
        #length = len(self.row_index)
        for i in range(0, self.m):
            a = [0 for x in range(0, self.n)]
            if i + 1 >= self.m :    # the last row
                n = len(self.row_info)
            else:
                n = self.row_index[i+1]
            
            for x in range(self.row_index[i], n):
                a[self.row_info[x].col] = self.row_info[x].val

            print(a)

        print("row info ->")
        print(self.row_index)
        for x in self.row_info:
            print(x.col, x.val)

        print("col info ->")
        print(self.col_index)
        for y in self.col_info:
            print(y.row, y.pos)

        #print(self.col_info)


    def __add(self, y) -> None:
        row_info = []  # 对应的非零元素的列号和数值表[列号, 元素的值]
        row_index = [0 for i in range(0, self.m)]         # 对应的每一行非零元素的起始位置 
        col_info = []  # 对应的非零元素的行号和元素所在row_info中的位置[行号，元素所在的位置]
        col_index = [0 for i in range(0, self.n)]         # 对应的每一列非零元素索引在col_info中的位置
        
        # rebuild self row_index, row_info, col_index, col_info
        # loop rows
        for i in range(0, self.m):
            x_begin_col = self.row_index[i]
            y_begin_col = y.row_index[i]
            if i >= (self.m - 1):   # last row
                x_end_col = len(self.row_info)
                y_end_col = len(y.row_info)
            else:
                x_end_col = self.row_index[i+1]
                y_end_col = y.row_index[i+1]

            # loop cols
            while (x_begin_col < x_end_col) and (y_begin_col < y_end_col):
                if self.row_info[x_begin_col].col < y.row_info[y_begin_col].col :
                    row_info.append( RowInfo(self.row_info[x_begin_col].col, self.row_info[x_begin_col].val) )
                    x_begin_col += 1
                elif self.row_info[x_begin_col].col > y.row_info[y_begin_col].col :
                    row_info.append( RowInfo(y.row_info[y_begin_col].col, y.row_info[y_begin_col].val) )
                    y_begin_col += 1
                else:
                    row_info.append( RowInfo(y.row_info[y_begin_col].col, self.row_info[x_begin_col].val + y.row_info[y_begin_col].val) )
                    x_begin_col += 1
                    y_begin_col += 1

            while (x_begin_col < x_end_col):
                row_info.append( RowInfo(self.row_info[x_begin_col].col, self.row_info[x_begin_col].val) )
                x_begin_col += 1

            while (y_begin_col < y_end_col):
                row_info.append( RowInfo(y.row_info[y_begin_col].col, y.row_info[y_begin_col].val) )
                y_begin_col += 1

            # 下一行的开始就是当前的末尾
            if (i + 1) < self.m :
                row_index[i+1] = len(row_info)

        self.row_info.clear()
        self.row_info = row_info.copy()
        self.row_index = row_index.copy()

        # build index of cols
        self.col_index = [0 for i in range(0, self.n)]
        self.col_info.clear()

        for i in range(0, self.m): # 遍历 表3.6, i 为行号
            if i == self.m - 1 :  # the last row
                last_row = len(self.row_info)
            else:
                last_row = self.row_index[i+1]
            for j in range(self.row_index[i], last_row): # 遍历一行所有的非零列
                if self.row_info[j].col >= (self.n - 1): # the last col
                    self.col_info.append(ColInfo(i, j))
                else:   # 插入下一列的前面，后面的位置都+1
                    self.col_info.insert(self.col_index[self.row_info[j].col + 1], ColInfo(i, j))
                    for k in range(self.row_info[j].col + 1, self.n):
                        self.col_index[k] += 1


    def add(self, x, y = None) -> None:
        if y is None :
            return self.__add(x)

        # loop rows
        for i in range(0, x.m):
            a = [0 for k in range(0, x.n)]
            x_begin_col = x.row_index[i]
            y_begin_col = y.row_index[i]
            if i >= (x.m - 1):   # last row
                x_end_col = len(x.row_info)
                y_end_col = len(y.row_info)
            else:
                x_end_col = x.row_index[i+1]
                y_end_col = y.row_index[i+1]

            # loop cols
            while (x_begin_col < x_end_col) and (y_begin_col < y_end_col):
                if x.row_info[x_begin_col].col < y.row_info[y_begin_col].col :
                    a[x.row_info[x_begin_col].col] = x.row_info[x_begin_col].val
                    x_begin_col += 1
                elif x.row_info[x_begin_col].col > y.row_info[y_begin_col].col :
                    a[y.row_info[y_begin_col].col] = y.row_info[y_begin_col].val
                    y_begin_col += 1
                else:
                    a[y.row_info[y_begin_col].col] = x.row_info[x_begin_col].val + y.row_info[y_begin_col].val
                    x_begin_col += 1
                    y_begin_col += 1

            while (x_begin_col < x_end_col):
                a[x.row_info[x_begin_col].col] = x.row_info[x_begin_col].val
                x_begin_col += 1

            while (y_begin_col < y_end_col):
                a[y.row_info[y_begin_col].col] = y.row_info[y_begin_col].val
                y_begin_col += 1

            #print(a)


'''
    test funtions
'''
if __name__ == "__main__":
    X = [
        [0,  2,  4, 0,  0,  0,  3],
        [-1, 0,  2, 0,  0,  1,  0],
        [10, -2, 0, 0, 10,  0,  0],
        [0,  0,  0, 0,  0, 10, -1]
    ]

    Y = [
        [0,  2,  4, 0,  0,  0,  9],
        [-1, 0,  2, 0,  0,  1,  0],
        [0,  0,  0, 0,  0,  0,  0],
        [6,  0,  0, 5,  0, 10, -1]
    ]

    # run X + Y by numpy as sample, check my algo
    a = np.array(X)
    b = np.array(Y)

    print( a + b )
    x = spare_matrix(X, 4, 7)
    #x.print()

    y = spare_matrix(Y, 4, 7)
    #y.print()

    x.add(y)
    x.print()

    #z = spare_matrix()
    #z.add(x, y)
    #z.print()
