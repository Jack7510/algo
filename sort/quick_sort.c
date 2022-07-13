//
// algo for quick sort.
// auth: Jack 
// date: July 7, 2022
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SWAP( a, b, x ) { x = a; a = b; b = x; }

//
// quick sort algo. 
// param
//  a[] - the array to be sorted
//  n   - the size of a[]
//

//
// partition
// a[] - array to be partition
// n   - the size of a[]
// pivot - return the index of pivot
//
int partition(int a[], int n, int* pivot)
{
    int left, right, p, temp;

    left = 0;
    right = n-1;
    p = left;

    while ( left != right )
    {
        // check pivot with right members
        if( left == p )
        {
            if(a[right] <= a[p])
            {
                SWAP(a[p], a[right], temp); // move smaller to the left of [p]
                p = right;
                left++;
            } 
            else
            {
                right--; // the pointer of right move to left
            }
        }
        else
        {
            //if( right == p )
            if(a[left] > a[p])
            {
                SWAP( a[left], a[p], temp ); // move bigger to the right of [p]
                p = left;
                right--;
            }
            else
            {
                left++;         // the pointer of left move to right
            }
        }
    }

    *pivot = left;

    return 0;
}



int quick_sort(int a[], int n)
{
    int left, right, pivot;

    if( n <= 1 ) return -1;

    // partition with a[0]
    partition(a, n, &pivot);
    
    quick_sort(a, pivot);   // sort left
    
    // sort the remaining part
    quick_sort(&a[pivot + 1], n - pivot - 1);
    
    return 0;
}

//
// stub routine for debug
//
void print_a(int a[], int n)
{
    int i;

    for( i = 0; i < n; i++ ) printf("%d ", a[i]);
    printf("\n");
}


int a_unsort[100] = {5, 7, 1, 8, 4, 3, 2};
//int a_unsort[100];

//
// usage: qsort arrays 
// e.g. qsort 1 5 3 7 6 8 0
//
int main(int argc, char* argv[])
{
    int n = 7;

    if( argc > 1 )
    {
        int i;

        memset(a_unsort, 0, sizeof(a_unsort));

        for( i = 1; i < argc; i++)
        {
            a_unsort[i-1] = atoi(argv[i]);
        }
        n = argc - 1;
    }

    print_a(a_unsort, n);
    quick_sort(a_unsort, n);
    print_a(a_unsort, n);

    return 0;
}