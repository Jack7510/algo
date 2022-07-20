# binary search

from turtle import left, right


def search(a: list, key: int, func = None) -> int :
    n = len(a)

    for i in range(0, n):
        if func != None :
            if key == func(a[i]) :
                return i
        else:
            if key == a[i] :
                return i

    return -1


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
    test function
'''
if __name__ == "__main__":

    a = [1,2,3,4,5,6,7,8,9]

    print("list ", a, "key ", 4, "pos ",  search(a, 4))
    print("list ", a, "key ", 4, "pos ",  binary_search(a, 4))
    print("list ", a, "key ", -1, "pos ",  search(a, -1))
    print("list ", a, "key ", -1, "pos ",  binary_search(a, -1))
    print("list ", a, "key ", 11, "pos ",  binary_search(a, 11))
    print("list ", a, "key ", 1, "pos ",  binary_search(a, 1))
    print("list ", a, "key ", 9, "pos ",  binary_search(a, 9))
    
    
    b = [ [1, -1], [2, -3], [4, 6], [5, 10]]
    print( b, search(b, 2, lambda x: x[0]))
    print( b, search(b, 5, lambda x: x[0]))
    