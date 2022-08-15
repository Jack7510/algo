'''
《计算之魂》 分治思想及应用

实现堆的基本操作，然后再做例题和习题

author: Jack Lee
date:   Aug 14, 2022 

version 1: 中值问题
    例题 6.4 给定一个非常巨大的数组，如何找到它的中值(Mediaum Value). 注意，中值不是平均值，而是指一半元素
    比它大，另一半元素比它小

    ex 6.4a: To support distribute computing, this example implement a method with 
    multiple CPU with multiple processes.
'''

from multiprocessing import Process, Queue, current_process, freeze_support

#
# Function run by worker processes
#

def worker(input, output):
    for func, args in iter(input.get, 'STOP'):
        result = calculate(func, args)
        output.put(result)

#
# Function used to calculate result
#

def calculate(func, args):
    result = func(*args)
    #print( '%s says that %s%s = %s' % \
    #    (current_process().name, func.__name__, args, result))
    return result

#
# Functions referenced by tasks
#

def partition(a, start, end, pivot):

    # skip the pivot
    left = start    
    right = end
    
    while True:
        # 从左边开始，寻找第一个比pivot大的元素
        while a[left] <= pivot and left < right :
            left += 1
        
        # 从右边开始，寻找第一个比pivot小的元素
        while a[right] >= pivot and right > start:
            right -= 1
        
        if left < right :
            a[left], a[right] = a[right], a[left]

            left += 1
            right -= 1
        else :
            break
    
    # if the a[start] is the max
    if a[start] > a[right] :
        a[start], a[right] = a[right], a[start]

    return a, start, end, right


# handle by one thread
def partition_by_ratio(a, start, end, target_position) :
    left_subarray_end = 0

    print("from %d -> %d \n", start, end);
    pivot = a[start]
    x0, x1, x2, left_subarray_end = partition(a, start, end, pivot)
    print(a, "\n")
    #//printf("left_sub_end %d\n", left_subarray_end);

    if left_subarray_end == target_position :
        return

    if left_subarray_end < target_position :
        partition_by_ratio(a, left_subarray_end + 1, end, target_position)
    else:
        partition_by_ratio(a, start, left_subarray_end - 1, target_position)


#
#
#

def test():

    a1 = [27, 17,  3, 16, 13,-10, 1]
    a2 = [5,   7, 12,  4, -8,  9, 0]
    a3 = [20, -3, -4, -5, 10, 33, -1]
    a4 = [71, 41,  6,  8, 21, 30, -9]

    a = [a1, a2, a3, a4]
    NUMBER_OF_PROCESSES = 4

    #a = [a1, a2] #, a3, a4]
    #NUMBER_OF_PROCESSES = 2

    data_length = 0
    for i in range( NUMBER_OF_PROCESSES ):
        data_length += len(a[i])
   
    section_length = len(a1)
    target_position = data_length // 2

    
    # Create queues
    task_queue = Queue()
    done_queue = Queue()

    # Start worker processes
    p = []
    for i in range(NUMBER_OF_PROCESSES):
        pid = Process(target=worker, args=(task_queue, done_queue))
        pid.start()
        p.append(pid)

    # pivot a1[0] as initial partition( a[], start, end, pivot)
    pivot = a1[0]
    TASKS1 = [(partition, (sub_a, 0, section_length - 1, pivot)) for sub_a in a]
    RESULT1 = []
    
    while True:

        # call partition()
        # Submit tasks
        
        for task in TASKS1:
            task_queue.put(task)

        # Get and print results
        RESULT1.clear()
        for i in range(len(TASKS1)):
            RESULT1.append(done_queue.get())
        

        '''
        RESULT1.clear()
        for func, args in TASKS1:
            # args[0] = sub_a[], args[1] = start, args[2] = end, args[3] = pivot 
            result = partition(args[0], args[1], args[2], args[3] )
            RESULT1.append(result)
        '''

        print("pivot: ", pivot)
        print( RESULT1 )

        left_subarray_end = 0
        for sub_a, start, end, right in RESULT1 :
            left_subarray_end += right + 1  # add 1 because array index from 0
    
        # analyse the result, build next tasks
        if left_subarray_end == target_position :
            break
        
        pre_pivot = pivot
        TASKS1.clear()
        section_length = 0

        if left_subarray_end < target_position :
            for sub_a, start, end, right in RESULT1:
                # pick up pivot from the longest section
                if section_length < (end - right) :
                    section_length = end - right

                    if right < end and sub_a[right] == pre_pivot:  # not the last one
                        pivot = sub_a[right + 1]                        # a1[left_subarray_end]
                        section_length -= 1
                    else:
                        pivot = sub_a[right]                            # a1[left_subarray_end]
          
            for sub_a, start, end, right in RESULT1:          
                if sub_a[right] == pre_pivot :
                    TASKS1.append((partition, (sub_a, right + 1, end, pivot)))
                else:
                    TASKS1.append((partition, (sub_a, right, end, pivot)))

            # partition( a[], left_sub_end, end, pivot )
        else:
            for sub_a, start, end, right in RESULT1:
                # pick up pivot from the longest section
                if section_length < (right - start) :
                    section_length = right - start

                    if sub_a[start] == pre_pivot :
                        pivot = sub_a[start + 1]
                        section_length -= 1
                    else:
                        pivot = sub_a[start]
                    
            for sub_a, start, end, right in RESULT1:
                if sub_a[start] == pre_pivot :
                    TASKS1.append((partition, (sub_a, start, right - 1, pivot)))
                else:
                    TASKS1.append((partition, (sub_a, start, right, pivot)))

    print("pivot: ", pivot)
    
    # Tell child processes to stop
    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')

    # wait all processes terminate.
    for pid in p:
        pid.join()


def test2():

    #a1 = [27, 17,  3, 16, 13,-10, 1]
    a1 = [27, 17,  3, 16, 13,-10, 1, 5,   7, 12,  4, -8,  9, 0,20, -3, -4, -5, 10, 33, -1, 71, 41,  6,  8, 21, 30, -9]
    a2 = [5,   7, 12,  4, -8,  9, 0]
    a3 = [20, -3, -4, -5, 10, 33, -1]
    a4 = [71, 41,  6,  8, 21, 30, -9]

    target_position = len(a1) // 2 
    partition_by_ratio(a1, 0, len(a1) - 1, target_position)

    print(a1, "\n")
    print(a1[target_position])



if __name__ == '__main__':
    freeze_support()
    test()
    #test2()
