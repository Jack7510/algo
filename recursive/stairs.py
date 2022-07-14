#!/usr/bin/python3

'''
//
// 思考题 2.1 上台阶问题的扩展
//   有n级台阶， 每次能够上k级，有多少种不同的攀登方法？
//   提示：走到第n级，上一次可能处在第n-1, n-2, ..., n-k 级
//
// auth: Jack
// date: July 14, 2022
//
'''

from locale import atoi
import sys

# global ways, how many ways can reach the top
global g_ways


'''
climb_stairs(track_list, n, k)
track_list - list of tracking
n - how many steps
k - 1 ~ k steps each time, k < n
'''
def climb_stairs(track_list: list, n: int, k: int) -> None:
    global g_ways

    if n == 0 :
        # reach the end, it is a way, +1.
        g_ways += 1

        # dump the track list
        track_list.append(0)
        print(track_list)
        track_list.clear()
        return
    
    if n > 0 :
        # not the end, append the mark
        track_list.append(n)

        #from 1 ~ k, if n - i < 0, do nothing
        for i in range(1, k+1):
            climb_stairs(track_list[:], n-i, k)
        
        return

    # if n < 0, do nothing
    return

'''
    test function
'''
if __name__ == "__main__":

    n = 5
    k = 2
    track_list = []
    g_ways = 0

    if len(sys.argv) >= 3:
        n = atoi(sys.argv[1])
        k = atoi(sys.argv[2])

    climb_stairs(track_list, n, k)
    print('stairs %d, step %d, ways %d' % (n, k, g_ways))