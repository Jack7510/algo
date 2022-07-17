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
    sum_max = [0, 0, a[0]]      # [left, right, Sum]

    # calc all intervals from 0 -> n-1
    for i in range(0, n):
        # init sum
        t = a[i]
        for j in range(i+1, n):
            # calc sum from i to j
            t += a[j]
            if t > sum_max[2] :      # if sum is max, store
                sum_max = [i, j, t]

    return sum_max


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
solve the problem with linear algo
para: 
a - the array of real number
p - the begin of a[]
q - the end of a[]

return:
p1 - the left boundary
q1 - the right bondary
S(p1, q1) < 0

max1 - the sum of the interval
l1 - == p1
r1 - right boundary of max1
'''
def max_sum_interval_linear(a: list):
    p = 0       # the begin of a[]
    K = len(a)  # length of a[]
    sum_max = [0, 0, a[0]]  # keep the sum interval
    
    while True :
        # STEP1: find the first positive number > 0
        p_i = -1
        for i in range(p, K) :
            if a[i] > sum_max[2] :
                sum_max = i, i, a[i]
            
            # a[i] > 0, stop loop
            if a[i] > 0 :
                p_i = i
                break
        
        # if p reach the end of a[], stop
        if p_i < 0 : # all items are less than 0
            return sum_max
        else: 
            p = p_i
        
        # STEP2: from left to right, calc [max_i, l1, r1], stop when s(p_i, q_i) < 0
        l_i = p
        s_i = a[p]
        p_i = -1
        for i in range(p+1, K):
            s_i += a[i]
            if s_i < 0 :        # s(l, r) < 0, stop
                p_i = i
                break

            # STPE3: if max_i is the max, keep it.
            if s_i > sum_max[2] :
                sum_max = l_i, i, s_i   # [l, r, s]
        
        # goto STEP1 until the end of a[]
        
        # if p reach the end of a[], stop
        if p_i < 0 : # all items are less than 0
            return sum_max
        else: 
            p = p_i
        
    return


'''
    test function
'''
if __name__ == "__main__":
    a = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]

    print('Example 1.3 max sum interval')
    print("Ex1: ", a)
    print("T(n) = n ** 2: ", max_sum_interval_v1(a))

    print("T(n) = n * log(n), Recurvise :", max_sum_interval_recursive(a, 0, len(a) - 1))

    print("T(n) = n, linear algo :", max_sum_interval_linear(a))

    b = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -62.2, 44.2, 5.4, -7.8, 1.1, -4.9]
    print("Ex2: ", b)
    print("T(n) = n ** 2: ", max_sum_interval_v1(b))

    print("T(n) = n * log(n), Recurvise :", max_sum_interval_recursive(b, 0, len(b) - 1))

    print("T(n) = n, linear algo :", max_sum_interval_linear(b))