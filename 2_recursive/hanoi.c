//
// algo for Hanoi problem.
// auth: Jack 
// date: July 10, 2022
//


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SWAP( a, b, x ) { x = a; a = b; b = x; }


//
// stub routine for debug
//
void print_a(int a[], int n)
{
    int i;

    for( i = 0; i < n; i++ ) printf("%d ", a[i]);
    printf("\n");
}


//#define MAX_HIGH 8
//int g_a[MAX_HIGH] = {8,7,6,5,4,3,2,1};
#define MAX_HIGH 5
int g_a[MAX_HIGH] = {5,4,3,2,1};
int g_b[MAX_HIGH];
int g_t[MAX_HIGH];


void print_all(void)
{
    print_a(g_a, MAX_HIGH);
    print_a(g_b, MAX_HIGH);
    print_a(g_t, MAX_HIGH);
    printf("------------\n\n");
}


//
// Hanoi problem algo. 
// hanoi( n, a, b, t )
//  func: move n members from a to b, with t as temp.
//  n   - how many members will be moved.
//  a[] - the array to be moved
//  b[] - the array to be stored members from a
//  t[] - the temporary array
//
void hanoi( int n, int a[], int b[], int t[])
{
    //
    // if n == 1, just move a[0] -> the top of b[]
    //
    if( n == 1 ) {
        b[0] = a[0];

        // for debug
        a[0] = 0;
        print_all();

        return ;
    }

    //
    // move a[1 ~ n-1] to the top of t[] with b[] as temporary
    //
    hanoi(n - 1, &a[1], t, b);

    //
    // move a[0] to the top of b[]
    //
    hanoi(1, a, b, t);

    //
    // move t[] to the top of b[] with a[] as temporary
    //
    hanoi(n - 1, t, &b[1], a);
}


//
// usage: hanoi n
// e.g. hanoi 8 or hanoi 64
//
int main(int argc, char* argv[])
{
    int n = MAX_HIGH;

    memset(g_b, 0, sizeof(g_b));
    memset(g_t, 0, sizeof(g_t));

    hanoi(MAX_HIGH, g_a, g_b, g_t);

    print_all();

    return 0;
}