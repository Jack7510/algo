/*
《计算之魂》 分治思想及应用

实现堆的基本操作，然后再做例题和习题

author: Jack Lee
date:   Aug 13, 2022 

version 1: 中值问题
    例题 6.4 给定一个非常巨大的数组，如何找到它的中值(Mediaum Value). 注意，中值不是平均值，而是指一半元素
    比它大，另一半元素比它小
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <vector>

using namespace std;

#define SWAP( a, b, x ) { x = a; a = b; b = x; }

void print_a(int a[], int start, int end)
{
    for(int i = start; i <= end; i++)
        printf("%d ", a[i]);

    printf("\n");
}


//
// partition
// a[] - array to be partition
// n   - the size of a[]
// pivot - return the index of pivot
//
int partition(int a[], int begin, int end, int* position)
{
    int left, right, p, temp;
    int pivot;

    left = begin + 1;
    right = end;
    pivot = a[begin];       // 采用第一个

    while ( 1 )
    {
        // 从左边开始，寻找第一个比pivot大的元素
        while ( a[left] < pivot && left < right )
        {
            left++;
        }
        
        // 从右边开始，寻找第一个比pivot小的元素
        while ( a[right] > pivot )
        {
            right--;
        }
        
        if( left < right )
        {
            SWAP(a[left], a[right], temp);
            left++;
            right--;
        }
        else 
            break;
    }

    SWAP(a[begin], a[right], temp);
    *position = right;

    return 0;
}


//
// partition_by_ration( a, 0, n-1, n/2)
//
void partition_by_ratio(int a[], int begin, int end, int target_position )
{
    int left_subarray_end = 0;

    //printf("from %d -> %d \n", begin, end);
    partition(a, begin, end, &left_subarray_end);
    //print_a(a, begin, end);
    //printf("left_sub_end %d\n", left_subarray_end);

    if( left_subarray_end == target_position )
        return ;

    if( left_subarray_end < target_position )
        partition_by_ratio(a, left_subarray_end + 1, end, target_position);
    else
        partition_by_ratio(a, begin, left_subarray_end - 1, target_position);
}


int main(int argc, char* argv[])
{
    int a[] = {27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0};
    //int a[] = {20, 3, -4, -5, 10, 33, 0, 71, 41, 6, 8, 21, 30, 9};
    int n = sizeof(a) / sizeof(a[0]);

    print_a(a, 0, n-1);
    
    partition_by_ratio(a, 0, n-1, n/2 );

    print_a(a, 0, n-1);
    printf("%d\n", a[n/2]);

    return 0;
}
