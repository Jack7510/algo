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
solve the problem with recursive algo
para: 
a - the array of real number

return:
p - the left boundary
q - the right bondary
s - the sum of the interval
'''
def max_sum_interval_recursive(a: list, p, q):
    n = q - p

    # only one
    if n == 0 :
        return p, q, a[p]

    else :
        # handle the left part[p, p + n / 2]
        p1, q1, s1 = max_sum_interval_recursive(a, p, p + n//2)
        #print(p, p + n//2, p1, q1, s1)
        
        # handle the right part[p + n / 2 + 1]
        p2, q2, s2 = max_sum_interval_recursive(a, p + n//2 + 1, q)
        #print(p + n//2 + n%2, q, p2, q2, s2)

        # 2 parts are connected and s1 > 0, s2 > 0
        if (p2 == q1 + 1) :
            if(s1 > 0) and (s2 > 0):
                return p1, q2, s1 + s2

        else:   # not connected 
            '''
            2 parts are seperated, the max(s1, s2, s3)
            s1 = [p1, q1]
            s2 = [p2, q2]
            s3 = [p1, q2]
            '''
            s3 = 0.0
            for i in range(q1+1, p2):
                s3 += a[i]
            s3 = s3 + s1 + s2
            if (s3 > s1) and (s3 > s2) :
                return p1, q2, s3

        if s1 > s2 :
            return p1, q1, s1
        else:
            return p2, q2, s2


'''
    test function
'''
if __name__ == "__main__":
    a = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]

    print('Example 1.3 max sum interval')
    print(a)
    print(max_sum_interval_v1(a))

    print(max_sum_interval_recursive(a, 0, len(a) - 1))
