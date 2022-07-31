'''
《计算之魂》 思考题4.4
    北京的街道通常是横平竖直的。假如你站在某个十字路口，需要往东，往北各走N个街区，有多少种不同的走法

Author: Jack Lee
Date:   July 31, 2022

Description:
    采用递归方法 S(L,N) = S(L, N-1) + S(L-1, N) ;
    S(0, X) = 1;
    S(X, 0) = 1;

History: 
July 31, 2022, version 1.0

'''

def s(l, n):
    return 1


'''
    test funtions
'''
if __name__ == "__main__":
    
    print("1, %d", s(1,1))
    print("2, %d", s(2,2))
    print("2, %d", s(3,3))
    print("2, %d", s(3,3))