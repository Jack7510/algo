'''
《计算之魂》 第九章 状态与流程

思考题 9.1 排豆子问题

author: Jack Lee
date:   Aug 19, 2022 

version 1: 

'''

import numpy as np


'''
思考题 9.1 排豆子算法
'''
class Robot:
    def __init__(self, a, x, y) -> None:
        self.grid = a       # the grid matrix 
        self.x = x          # robot's position(x, y)
        self.y = y
        self.beans = 0      # how many beans the robot has picked.

    def pick_up(self):
        if self.grid[self.y][self.x] != 0 :
            self.beans += 1
            self.grid[self.y][self.x] -= 1
            return True
        else:
            return False

    def drop(self):
        if self.beans > 0 and self.grid[self.y][self.x] == 0 :
            self.beans -= 1
            self.grid[self.y][self.x] += 1
            return True
        else:
            return False

    def move_left(self):
        self.x -= 1
        if self.x < 0 :
            self.x = 0
            return False
        else:
            return True

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y -= 1
        if self.y < 0 :
            self.y = 0
            return False
        else:
            return True

    def move_up(self):
        self.y += 1
        if self.y >= len(self.grid) :
            self.y -= 1
            return False
        else:
            return True

    '''
    move robot to the top of the col y in a[]
    '''
    def move_to_top(self):
        while True:
            if self.is_occupied() is True :
                if self.move_up() is False:
                    return
            else:   
                # 当前格子为空，已经到顶，往下退一步
                self.move_down()
                return

    '''
    整列为空，表示到达右边界，返回True
    '''
    def col_is_null(self):
        while self.is_occupied() is False:
            
            # 到底了
            if self.move_down() is False:
                return True
        
        return False

    '''
    有豆子，返回True
    '''
    def is_occupied(self):
        if self.pick_up() is True:
            self.drop()
            return True
        
        return False

    '''
    当前列的豆子数比左边列的豆子数少, 返回TRUE
    '''
    def col_left_is_gt(self):
        # right is bigger by default
        left_is_gt = False

        self.move_to_top()
        if self.move_left() :
            # 如果左边的格子为空，表示left < right
            if self.is_occupied() is False :
                left_is_gt = False
            else:
                # 再往上走一步，看看是否还有豆子，如果还有，左边 > 右边
                if self.move_up() is True:
                    if self.is_occupied() is True:
                        left_is_gt = True
                self.move_down()
                
        self.move_right()       # back to right
        return left_is_gt
        
    '''
    把当前列和左边的交互，仅仅搬动最上方的豆子
    '''
    def swap_with_left(self):
        self.move_left()  # 在左列的最高端
        self.move_to_top()

        while True:
            self.pick_up()
            self.move_right()
            if self.drop() is False:
                # the job is done, put it back
                self.move_left()
                self.drop()
                #self.move_right()
                break
            else:
                self.move_left()
                self.move_down()


    '''
    从右到左，重新排各列
    '''
    def sort_beans_from_right_left(self):
        while True:
            self.swap_with_left()
            if self.move_left() is False:   # left boundary
                return
            
            self.move_right()
            if self.col_left_is_gt() is False:
                return


def sort_beans(a):
    # robot from left_bottom corner
    robot = Robot(a, 0, 0)

    # move to the top of column robot_y
    while True:
        robot.move_right()
        
        # 如果整列为空，到了右边界
        if robot.col_is_null() :
            return

        # 如果比左列的豆子多, right > left, next
        if robot.col_left_is_gt() is False:
            continue

        # 左边比右边大，需要调换位置
        robot.sort_beans_from_right_left()


if __name__ == "__main__" :
    a1 = [ \
        [0, 0, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 1, 1, 0, 0], \
        [0, 1, 0, 1, 1, 1, 1, 0, 0], \
        [1, 1, 0, 1, 1, 1, 1, 0, 0], \
        [1, 1, 1, 1, 1, 1, 1, 0, 0]  \
    ]

    a2 = [ \
        [0, 0, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 1, 1, 0, 0], \
        [0, 1, 0, 1, 1, 1, 1, 0, 0], \
        [1, 1, 0, 1, 1, 1, 1, 1, 0], \
        [1, 1, 1, 1, 1, 1, 1, 1, 0]  \
    ]

    a = a2
    
    a.reverse()
    sort_beans(a)

    # 为了看起来清晰，把矩阵倒过来看
    a.reverse()
    print(np.array(a))

    