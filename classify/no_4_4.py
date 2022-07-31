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

'''
计算向左走left个街区，向北走north个街区的走法
当left或者north为0时，我们只有一种方法，走直线
'''
def s(left, north):
    if left == 0 or north == 0:
        return 1
    
    return s(left, north-1) + s(left-1, north)


'''
    test funtions
'''
if __name__ == "__main__":
    
    print("N = 1", s(1,1))
    print("N = 2", s(2,2))
    print("N = 3", s(3,3))
    print("N = 4", s(4,4))