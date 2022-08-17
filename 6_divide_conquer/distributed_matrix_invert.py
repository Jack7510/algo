'''
《计算之魂》 分治思想及应用

分布式对矩阵求逆。矩阵超级大

author: Jack Lee
date:   Aug 16, 2022 

version 1: 矩阵求逆
    思考题 6.4 如何用多台服务器实现大规模求逆

version 2: Aug 17
    改进昨天的算法，去掉了元素为0的处理。矩阵 3 * 3, V1 需要90次运算。V2 只需要60次
'''

import numpy as np
import numpy.matlib


'''
matrix_invert_algo(a, a_identity)
a - matrix to be inverted
a_identity - identity, dimension same as a

return
a - become identity
a_identity - become invert matrix a
'''
def matrix_invert_algo(a, a_identity):
    dimension = len(a)
    count = 0

    for i in range(0, dimension):
        a_ii = a[i][i]
        # handle #i row first A1 = A1 / a11
        for l in range(0, dimension):
            a[i][l] = a[i][l] / a_ii     # a[i,i] = 1
            a_identity[i][l] = a_identity[i][l] / a_ii
            count += 2

        # handle row except i#
        for j in range(0, dimension):
            if j == i :
                continue

            # handle each col 0 - n - 1
            # Aj = Aj - Ai * a[j, i]
            a_ji = a[j][i]
            for k in range(0, dimension):
                a[j][k] = a[j][k] - a[i][k] * a_ji  # a[]
                a_identity[j][k] -= a_identity[i][k] * a_ji
                count += 4
    
    print("v1 count =", count)


'''
功能和上面的函数一样，只是为了降低运算的冗余。因为在矩阵中和单位矩阵中，有大量的0，无需多次计算。
a - 为n*n矩阵
a_identity - 为n*n 单位矩阵

返回
a - 为n*n单位矩阵
a_identity - 为n*n a的逆矩阵
'''
def matrix_invert_algo_v2(a, a_identity):
    n = len(a)
    count = 0

    # a[] 按行 从 i from 0 -> n - 1
    # set a_ii = 1, a[i] / a_ii, I_ii = 1 / a_ii
    # I[i] j from 0 -> i, I[i][j] / a_ii
    for i in range(0, n):
        a_ii = a[i][i]
        for j in range(i, n):   # a[i][0~i] is '0'
            a[i][j] /= a_ii
            count += 1

        for j in range(0, i+1): # I[i][i+1 ~ n-1] is '0'
            a_identity[i][j] /= a_ii
            count += 1

        # a[] i#列 j from 0 -> n - 1 (j != i)
        # set a_ji = 0, a[j] - a[i] * a[j][i]
        # I[j] - I[i] * a[j][i], 其中列从 0 - i  
        for j in range(0, n):   # top -> down
            if j == i : continue

            a_ji = a[j][i]
            for k in range(i, n): # left -> right, a[j][0 ~ i] is '0' 
                a[j][k] -= a[i][k] * a_ji
                count += 2

            for k in range(0, i+1): # I[i][i+1 ~ n-1] is '0'
                a_identity[j][k] -= a_identity[i][k] * a_ji
                count += 2

    print("v2 count = ", count)


def test_matrix_invert_algo():
    
    a1 = [ \
        [1, -1, -1], \
        [-1, 2, 3], \
        [1, 1, 4] \
    ]
    
    a2 = [ \
        [1, 0, 1], \
        [0, 2, 1], \
        [1, 1, 1] \
    ]

    a3 = [\
        [1, 2], \
        [-1, -3]\
    ]

    a = a3
    
    b = np.array(a)
    print("a = ")
    print(b)
    
    
    # make matrix identity
    a_identity = []
    for i in range(0, len(a)):
        a_identity.append( [0 for j in range(0, len(a))] )
        a_identity[i][i] = 1
    
    #matrix_invert_algo(a, a_identity)
    matrix_invert_algo_v2(a, a_identity)


    print("Invert by Jack:")
    print("a = ")
    print(np.array(a))
    print("Invert = ")
    print(np.array(a_identity))

    # make invert matrix
    print("invert by numpy")
    b_invert = np.linalg.inv(b)
    #print(b_invert)
    c = ( b_invert != np.array(a_identity) )
    if c.sum() == 0 :
        print("algo done.")
    else:
        print("algo wrong.")


def test_matrix_invert_distribute():
    pass


if __name__ == '__main__':
    test_matrix_invert_algo()

    test_matrix_invert_distribute()