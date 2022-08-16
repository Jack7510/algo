'''
《计算之魂》 分治思想及应用

分布式对矩阵求逆。矩阵超级大

author: Jack Lee
date:   Aug 16, 2022 

version 1: 矩阵求逆
    思考题 6.4 如何用多台服务器实现大规模求逆

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

    for i in range(0, dimension):
        a_ii = a[i][i]
        # handle #i row first A1 = A1 / a11
        for l in range(0, dimension):
            a[i][l] = a[i][l] / a_ii     # a[i,i] = 1
            a_identity[i][l] = a_identity[i][l] / a_ii

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
    print("matix ->")
    print(b)
    
    
    # make matrix identity
    a_identity = []
    for i in range(0, len(a)):
        a_identity.append( [0 for j in range(0, len(a))] )
        a_identity[i][i] = 1
    
    matrix_invert_algo(a, a_identity)

    print("invert by Jack:")
    print(np.array(a))
    print(np.array(a_identity))

    # make invert matrix
    print("invert by numpy")
    b_invert = np.linalg.inv(b)
    print(b_invert)


def test_matrix_invert_distribute():
    pass


if __name__ == '__main__':
    test_matrix_invert_algo()

    test_matrix_invert_distribute()