//
// algo for merge sort.
// auth: Jack 
// date: July 8, 2022
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SWAP( a, b, x ) { x = a; a = b; b = x; }

//
// merge sort algo. 
// param
//  a[] - the array to be sorted
//  n   - the size of a[]
//

//
// combine_2_parts()
// a[] - 
// n   - the size of a[]
// pivot - return the index of pivot
//
int combine_2_parts(int buff[], int buff_len, int a[], int n_a, int b[], int n_b)
{
    int p, q, i;

    p = 0;
    q = 0;
    i = 0;
    while( p < n_a || q < n_b ) {
        if( p >= n_a ) // a[] is end
        {
            buff[i] = b[q];
            i++;
            q++;
        } else if (q >= n_b) // b[] is end
        {
            buff[i] = a[p];
            i++;
            p++;
        }
        else
        {
            if(a[p] <= b[q]) {
                buff[i] = a[p];
                i++;
                p++;
            }
            else
            {
                buff[i] = b[q];
                i++;
                q++;
            }
        }
    }

    return 0;
}


//
// merge_sort, implementation of merge algo
//  a[] - the array to be sorted
//  n   - the length of a[]
//  b[] - sorted array result, size is n
// return 0
//
int merge_sort(int a[], int n, int b[])
{
    int* buff;

    if( n <= 1 ) {
        b[0] = a[0];
        return 0;
    }

    // divide into 2 parts
    merge_sort(a, n / 2, b);               // sort the first part
    
    merge_sort(&a[n/2], (n+1) / 2, &b[n/2]);     // sort second part
    
    // combine 2 parts
    buff = malloc(sizeof(b[0]) * n);
    if( buff == NULL ) return -1;
    
    combine_2_parts(buff, n, b, n/2, &b[n/2], (n+1)/2 );
    memcpy(b, buff, sizeof(b[0]) * n);
    free( buff );

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
int a_sort[100];
//int a_unsort[100];

//
// usage: merge_sort arrays 
// e.g. merge_sort 1 5 3 7 6 8 0
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
    merge_sort(a_unsort, n, a_sort);
    print_a(a_sort, n);

    return 0;
}