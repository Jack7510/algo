'''
《计算之魂》 
思考题 1.3 Q3. 在一个二维矩阵中，寻找一个矩形的区域，使其中的数字之和达到最大值

Author: Jack
Date: July 17, 2022
'''


# calc the sum of matrix
def calc_matrix_sum(a, x1, y1, x2, y2) -> int:
    sum = 0

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum += a[i][j]

    return sum


'''
v1 algo: 采用两重循环方法，时间复杂度 T(n) = O(n ** 4)
max_sum_matrix_v1(a, width, high) -> max_sum[i, j, width, high, sum]
param:
a[]  - the array 
width- the width of a[] x dimension
high - the high of a[], y dimension

return:
i,j  - the cordinate of left cornor
width, high - the size of the sub matrix
sum  - the sum of the sub matrix
'''
def max_sum_matrix_v1( a: list, width: int, high: int ) :
    max_sum = a[0][0]
    i, j = 0, 0
    delta_i, delta_j = 0, 0

    # calc all matrix[x1, y1, x2, y2], return the max
    for x1 in range(0, width) :
        for y1 in range(0, high) :
            for x2 in range(x1, width):
                for y2 in range(y1, high):
                    sum = calc_matrix_sum(a, x1, y1, x2, y2)
                    if sum > max_sum :
                        i, j, delta_i, delta_j, max_sum = x1, y1, x2, y2, sum
    
    return i, j, delta_i, delta_j, max_sum


'''
    test function
'''
if __name__ == "__main__":
    a = [
        [1, 2, 3, 4, 0, -5, 6, -7],
        [6, -5, 4, 3, 2, 2, 8, -1]
    ]
    
    print('Example 1.3 Q3 在一个二维矩阵中，寻找一个矩形的区域，使其中的数字之和达到最大值')
    print("Ex1: ", a)

    #x, y, width, high, sum = max_sum_matrix_v1(a, 8, 2)
    print("T(n) = n ** 4: ",  max_sum_matrix_v1(a, 2, 8) )
