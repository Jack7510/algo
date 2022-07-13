#!/usr/bin/python3

'''
//
// algo for Hanoi problem.
// auth: Jack 
// date: July 10, 2022
//
'''

'''
Solve Hanoi problem with recursive
'''

import sys

'''
func: hanoi()
para: 
    n - the numbers would be moved from source to target
    source - list to be moved
    targe - list as target
'''
def hanoi(n, source, target, temporary) :
    if n > 0 : 
        # move top n - 1 members from source to the top of temprary
        hanoi( n - 1, source, temporary, target)

        # move top source to the top of target
        target.append( source.pop() )
        print_status()

        # move n - 1 members from temporary to target
        hanoi( n - 1, temporary, target, source)
    return


#g_source = [4,3,2,1]
g_source = []
g_target = []
g_temporary = []


'''
    print all the list members
'''
def print_status() :
    print("A:", g_source)
    print("T:", g_temporary)
    print("B:", g_target)
    print("-------------\n")
    

'''
    test function
'''
if __name__ == "__main__":
    # init n members of g_source
    n = 4
    
    if len(sys.argv) > 1 :
        n = int(sys.argv[1])

    for x in range(n, 0, -1):
        g_source.append(x)

    print_status()
    hanoi(len(g_source), g_source, g_target, g_temporary)
