'''
《计算之魂》 思考题 5.3
    Q2 主干网的建设问题。

Author: Jack Lee
Date:   Aug 7, 2022

Description:
    二维坐标系上的点 P1(x1, y1), P2(x2, y2), ..., Pn(xn, yn). 现在要拉一根主干光纤，水平地穿过园区
    这根主干光纤放什么位置。使其到各栋大楼的总距离最短。

    答：经过证明，这根光纤的总距离和寻找某栋楼与其他楼的距离总和相同。我们假设这个点Pk(xk, yk)
    两个点Pa, Pb的y方向距离 d = abs( yb - ya )
    以点Pk为例，总距离为Sk = abs(yk - y1) + abs(yk - y2) + ... + abs(yk - yn), k = 1 .. n
    [S1, S2, .., Sn] 的最小值对应的点，就是答案。n为偶数时，最小值有2个。n为奇数时，最小值为1

    T(n) = O(n ** 2)

    估计还有复杂度更低的办法

History: 
Aug 7, 2022, version 1.0

'''

import random

def min_distance( p : list ) :
    s = []
    n = len(p)

    for i in range(0, n):
        yk = p[i]
        sk = 0
        for yi in p:
            sk += abs(yi - yk)
        s.append([sk, i])

    print(s)
    return sorted(s)[0]

    
'''
    test funtions
'''
if __name__ == "__main__":
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    sk = min_distance(p)
    print( "k = ", sk[1], "S = ", sk[0] )

    q = [ random.randrange(0, 100) for i in range(0,19)]
    print(q)
    sk = min_distance(q)
    print( "k = ", sk[1], "S = ", sk[0] )

