'''
《计算之魂》 
思考题 1.3 Q3. 在一个二维矩阵中，寻找一个矩形的区域，使其中的数字之和达到最大值

Author: Jack
Date: July 17, 2022
'''

global _g_count

# calc the sum of matrix
def calc_matrix_sum(a, x1, y1, x2, y2) -> int:
    global _g_count

    sum = 0

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum += a[i][j]
            _g_count += 1

    return sum


'''
v1 algo: 采用两重循环方法，时间复杂度 T(n) = O(n ** 4) 6次循环
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
optimize v1, 5次循环
'''
def max_sum_matrix_v2( a: list, high: int, width: int ) :
    global _g_count

    max_sum = a[0][0]
    i, j = 0, 0
    delta_i, delta_j = 0, 0

    # calc all matrix[x1, y1, x2, y2], return the max
    for y1 in range(0, high) :
        for x1 in range(0, width) :

            # calc all matrix from x1, y1, width, high
            for y2 in range(y1, high):

                # 逐列累加
                sum_sub_matrix = 0
                for x2 in range(x1, width):
                    #sum = calc_matrix_sum(a, x1, y1, x2, y2)
                    
                    # 计算一列
                    # calc line (x2, y1) -> (x2, y2)
                    for y_i in range(y1, y2 + 1):
                        sum_line = 0        # sum of a line
                        # from x1 -> x2
                        sum_line += a[y_i][x2]
                        _g_count += 1

                        # add one line each time
                        sum_sub_matrix += sum_line
                        if sum_sub_matrix > max_sum :
                            i, j, delta_i, delta_j, max_sum = y1, x1, y2, x2, sum_sub_matrix
        
    return i, j, delta_i, delta_j, max_sum


'''
algo 3: 纵向采用递归方法，把矩阵(m * n)分解为两个(m/2 * n)，递归分解，最后变成(1,n)矩阵。
通过例题 1.3的方法，求出(1,n)的最大区间，然后回到更高维度进行比较，每次得到最大区域
T(n) = n * n + n * log(n)
def max_sum_matrix_v2( a, begin, lines, width ) -> x1, y1, x2, y2, sum :

param:
a -- matrix to handle
begin -- index of beginning line
lines -- how many lines to handle
width -- the number of items of one line

return:
left upper corner(x1, y1)
right down corner(x2, y2)
sum - the sum of matrix(x1, y1, x2, y2)
'''
# include max_sum_interval.py
import max_sum_interval

# calc the sum of a small region T(n) = O(n**2)
def _calc_matrix_sum( a, x1, y1, x2, y2 ):
    tmp = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            tmp += a[i][j]
    
    return tmp


def max_sum_matrix_v3( a: list, begin: int, lines: int, width: int ) :

    # if only 1 line, end of recursive
    if lines == 1:
        s = max_sum_interval.max_sum_interval_linear(a[begin])
        return [ begin, s[0], begin, s[1], s[2] ]

    else:
        # slice a into 2 smaller parts and handle individually
        s1 = max_sum_matrix_v3(a, begin, lines // 2, width)
        s2 = max_sum_matrix_v3(a, begin + lines // 2, lines - lines // 2, width)
        
        # if s1 >0 and s2 > 0 return max( s1, s2, [s1, s2])
        if s1[-1] > 0 and s2[-1] > 0 :
            # calc [s1, s2]
            x1 = min(s1[0], s2[0])
            y1 = min(s1[1], s2[1])
            x2 = max(s1[2], s2[2])
            y2 = max(s1[3], s2[3])
            s3 = _calc_matrix_sum( a, x1, y1, x2, y2 )
            return [x1, y1, x2, y2, max(s1[-1], s2[-1], s3)]

        # else return max( s1, s2 )
        else:
            if s1[-1] > s2[-1] :
                return s1
            else: return s2
        

'''
    test function
'''
if __name__ == "__main__":
    a = [
        [1, 2, 3, 4, 0, -5, 6, -7],
        [6, -5, 4, 3, 2, 2, 8, -1],
        [33, -15, 14, 32, 12, 42, 18, -81]
    ]
        
    print('Example 1.3 Q3 在一个二维矩阵中，寻找一个矩形的区域，使其中的数字之和达到最大值')
    print("Ex1: ", a)

    #x, y, width, high, sum = max_sum_matrix_v1(a, 8, 2)
    _g_count = 0
    print("V1: ",  max_sum_matrix_v1(a, 3, 8), _g_count)
    
    _g_count = 0
    print("V2: ",  max_sum_matrix_v2(a, 3, 8), _g_count)
    
    _g_count = 0
    print("V3: ",  max_sum_matrix_v3(a, 0, 3, 8), _g_count)