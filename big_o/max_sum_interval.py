'''
《计算之魂》 例题 1.3 总和最大区间问题

Author: Jack
Date: July 16, 2022
'''


'''
algo with V1, the easy one
time complex = n ** 2 + n
'''
def max_sum_interval_v1(a: list):
    n = len(a)

    # p is the begin of interval, q is the end of interval
    p = q = 0
    sum_list = []

    # calc all intervals from 0 -> n-1
    for i in range(0, n):
        # init sum
        s = t = a[i]
        for j in range(i+1, n):
            # calc sum from i to j
            t += a[j]
            if t > s :      # if sum is max, store
                p, q, s = i, j, t

        # append the result to the list
        sum_list.append([p, q, s])
    
    # find out the max sum in sum_list
    k = 0
    for i in range(0, n) :
        if sum_list[i][2] > sum_list[k][2]:
            k = i

    return sum_list[k]


'''
    test function
'''
if __name__ == "__main__":
    a = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]

    print('Example 1.3 max sum interval')
    print(a)
    print(max_sum_interval_v1(a))
