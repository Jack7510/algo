'''
《计算之魂》 
思考题 1.3 Q2. 在一个数组中寻找一个区间，使得区间内的数字之和等于某个事先给定的数字.

Author: Jack
Date: July 17, 2022
'''

'''
v1 algo: 采用两重循环方法，时间复杂度 T(n) = O(n ** 2)
find_sum_interval_v1(a, sum) -> l, r, b_found
param:
a[]  - the array 
sum  - the sum to match the interval in a[]

return:
l    - the left boundary of the interval, -1 while not found
r    - the right boundary of the interval, -1 while not found
b_found - True if the interval is found
'''
def find_sum_interval_v1( a: list, sum: int ) :
    left = -1
    right = -1
    n = len(a)

    for i in range(0, n) :
        s = a[i]
        if s == sum :
            return i, i

        # calc s(i,j), if s(i,j) == sum, done
        for j in range(i+1, n) :
            s += a[j]
            if s == sum :
                return i, j
    
    # not found
    return -1, -1


'''
    test function
'''
if __name__ == "__main__":
    a = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 20, 10, 11, 19]
    sum = 39

    print('Example 1.3 find sum of the internal in a[]')
    print("Ex1: ", a, sum)
    left, right = find_sum_interval_v1(a, sum)
    print("T(n) = n ** 2: ", left, right, a[left : right+1])
