'''
《计算之魂》 思考题1.4 Q2. 区间排序

Author: Jack Lee
Date:   July 22, 2022

Description:
    区间排序，本质上还是排序，这次练习，采用merge sort的思想，先把N个区间分为N/2个区间，先排序这两个N/2 区间序列，迭代进行。
    当左右区间排好了，就合并。

    两个区间排序算法，需要单独编写，实现类似两个数大小比较

History: 
July 22, 2022, version 1.0

'''


'''
cmp_2_section(s1, s2)
func:
    if s1 > s2, return False
para:
    s1 - section 1, list
    s2 - section 2, list
'''
from turtle import right


def cmp_2_section(s1: list, s2: list):
    # include l1 < l2 , r2 < r1; s2 in s1
    if s1[0] <= s2[0] and s2[1] <= s1[1] :
        return True

    # s1 in s2: l2 <= l1 and r1 <= r2
    if s2[0] <= s1[0] and s1[1] <= s2[1] :
        return True

    # intersect s1 on left, s2 on right
    # not intersect s1 left, s2 right, s1[] < s2[]
    # l1 <= l2 and r1 <= r2,
    if s1[0] <= s2[0] and s1[1] <= s2[1]:
        return True

    # intersect s1 on right, s2 on left
    # l2 <= l1 and r2 <= r1, and r2 > l1
    if s2[0] <= s1[0] and s2[1] <= s1[1] and s2[1] > s1[0]:
        return True

    return False


'''
merge_sort(sectoins: list, key=cmp_func)
func:
    sort the sections with merge algo
para:
    sections - unsorted sections, list
    start    - index of sections beginning
    n        - numbers of section to be sorted
    key      - function to compare 2 sections, return True if sorted
return:
    None
'''
def merge_sort(sections: list, start: int, n: int, key=None):
    # if only 1 section, just return
    if n <= 1:
        return

    # sort left part and right part
    merge_sort(sections, start, n // 2, key)
    merge_sort(sections, start + n // 2, n - n // 2, key)
    
    # merge left & right
    tmp_sections = sections[start : start + n ]
    left, left_n = 0, n // 2
    right, right_n = n // 2, n
    begin = start
    while (left < left_n) and (right < right_n):
        if key(tmp_sections[left], tmp_sections[right]) :
            sections[begin] = tmp_sections[left]
            left += 1
        else:
            sections[begin] = tmp_sections[right]
            right += 1
        begin += 1

    # copy the remains of left part
    if left < left_n:
        for i in range(left, left_n) :
            sections[begin] = tmp_sections[i]
            begin += 1

    # copy the remain of right part
    if right < right_n:
        for i in range(right, right_n) :
            sections[begin] = tmp_sections[i]
            begin += 1


'''
    test funtions
'''
if __name__ == "__main__":
    a_sections = [[1, 4], [2, 3], [1.5, 2.5]]
    b_sections = [[2, 3], [1, 4], [1.5, 2.5]]
    c_sections = [[1, 2], [2.7, 3.5], [1.5, 2.5]]
    d_sections = [[1, 2], [2.7, 3.5], [1.5, 2.5], [0, 1], [2.3, 2.4], [1, 4], [3.5, 4.1]]

    '''
    print( a_sections )
    for i in range(len(a_sections) - 1):
        print("cmp ", a_sections[i], a_sections[i + 1], 
            cmp_2_section(a_sections[i], a_sections[i + 1]))
    
    print( b_sections )
    for i in range(len(b_sections) - 1):
        print("cmp ", b_sections[i], b_sections[i + 1], 
            cmp_2_section(b_sections[i], b_sections[i + 1]))

    print( c_sections )
    for i in range(len(c_sections) - 1):
        print("cmp ", c_sections[i], c_sections[i + 1], 
            cmp_2_section(c_sections[i], c_sections[i + 1]))
    '''

    print("merge sort sections")
    print(c_sections, '->')
    merge_sort(c_sections, 0, len(c_sections), cmp_2_section)
    print(c_sections)

    print(d_sections, '->')
    merge_sort(d_sections, 0, len(d_sections), cmp_2_section)
    print(d_sections)
