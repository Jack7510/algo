'''
《计算之魂》 
思考题 1.3 Q2. 在一个数组中寻找一个区间，使得区间内的数字之和等于某个事先给定的数字.

Author: Jack
Date: July 17, 2022

history:
Version 1.0 July 17, 2022 T(n) = O(n ** 2)
Version 1.1 July 18, 2022, T(n) = n + n * log(n) + log(n) ** 2
'''

'''
v1 algo: 采用两重循环方法，时间复杂度 T(n) = O(n ** 2)
find_sum_interval_v1(a, sum) -> l, r
param:
a[]  - the array 
sum  - the sum to match the interval in a[]

return:
l    - the left boundary of the interval, -1 while not found
r    - the right boundary of the interval, -1 while not found
'''
def find_sum_interval_v1(a: list, sum: int ) :
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
binary search algo, start from middle item, if key < [mid], search left half part, 
otherwise, right part
'''
def binary_search(a: list, key: int, func = None) -> int :
    n = len(a)
    left = 0
    right = n - 1
    
    while left <= right :
        mid = left + (right - left + 1) // 2
        if func != None :
            item = func(a[mid])
        else:
            item = a[mid]

        if item == key :
            return mid
        elif item < key :  # handle the right part
            left = mid + 1
        else : # handle the left part
            right = mid - 1

    return -1


'''
V2 algo: 
1. 构建一个新的list list_sum，[index, s(0, index)]. 从a的第一个元素开始到最后一个
   list_sum的每个成员[index, sum(a[0], a[index])], index是 a的成员索引
   sum((a[0], a[index])) = 从第一个元素到第index元素的总和
2. 把list_sum 按照item中的sum从小到大排序
3. 用二分法找到 list_sum[l][1] - list_sum[r][1] == K

find_k_interval_v2(a, K) -> l, r
param:
a[]  - the array 
k    - the sum to match the interval in a[]

return:
l    - the left boundary of the interval, -1 while not found
r    - the right boundary of the interval, -1 while not found
'''
def find_k_interval_v2(a: list, K: int) :
    
    # STEP 1 build list_sum, skip all 0 items  T(n) = n, 
    list_sum = []      # init list_sum with first item of a
    n = len(a)
    sum = 0
    for i in range(0, n):
        # skip all 0 items
        if a[i] != 0 :
            sum += a[i]
            list_sum.append([i, sum])

        # find out K = s[0..i]
        if sum == K :
            return 0, i
    
    # STEP 2 sort list_sum by 2nd element-sum. T(n) = n * log(n)
    list_sum.sort(key=(lambda x: x[1]))

    # STEP 3 find out K interval with binary search
    # T(n) = n * log(n)
    n = len(list_sum)
    #left = 0
    #right = n - 1
    
    #print(list_sum)

    if K > 0:
        for i in range(0, n - 1) :
            temp = list_sum[i][1] + K

            # if list_sum[i+1 : ], search should be improved
            '''
            for x in list_sum[i+1 :] :
                if temp == x[1] :
                    return list_sum[i][0] + 1, x[0]
                if temp < x[1] :
                    break
            '''
            # search with binary search
            pos = binary_search(list_sum[i+1 :], temp, lambda x:x[1])
            if pos >= 0 :
                return list_sum[i][0] + 1, list_sum[i+1+pos][0]

    else:
        # K < 0, 
        for i in range(n-1, 0, -1) :
            temp = list_sum[i][1] + K

            '''
            # if list_sum[i+1 : ], search should be improved
            for x in list_sum[:i-1] :
                if temp == x[1] :
                    return list_sum[i][0] + 1, x[0]
                if temp < x[1] :
                    break        
            '''

            # search with binary search
            pos = binary_search(list_sum[: i-1], temp, lambda x:x[1])
            if pos >= 0 :
                return list_sum[i][0] + 1, list_sum[pos][0]

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
    print("V1 T(n) = n ** 2: ", left, right, a[left : right+1])

    left, right = find_k_interval_v2(a, sum)
    print("V2 T(n) = n + n * log(n): ", left, right, a[left : right+1])
