/*
《计算之魂》 分治思想及应用

实现堆的基本操作，然后再做例题和习题

author: Jack Lee
date:   Aug 13, 2022 

version 1: 最大堆，最小堆，
version 2: top_k()
    例题 6.3：一个未排序的序列里有N个元素，如何找到其中最大的K个元素？
*/

#include <iostream>
#include <vector>

using namespace std;

class Heap {
public:
    vector<int>   a;      // heap array
    int  length; // heap array length
    int  heap_size;  // heap size

private:
    int  parent(int i);
    int  left(int i);
    int  right(int i);
    void swap(int i, int j);
    void max_heapify(int i);
    void min_heapify(int i);
    
public:
    void build_max_heap(void);
    void heap_sort(void);

    void build_min_heap(void);
    void heap_sort_reverse(void);
    void min_heapify_with_new_element(int n);

    void getHeap(vector<int>& b);
    //void set(int i, int v);
    void print(void);

    Heap(int size);
    Heap(const vector<int>& b, int size);

    ~Heap();
};

/*
Heap::Heap(int size)
{
    a = new int[size];
    length = size;
    heap_size = 0;
}
*/

Heap::Heap(const vector<int>& b, int size)
{
    a = b;
    length = size;
    heap_size = size;
}

Heap::~Heap()
{

}


//
// get i's parent index
// 取不大于 i / 2 的整数
// 以下的算法和《算法导论》不同，原因是索引从0开始
//
int Heap::parent(int i)
{
    return (i - 1) / 2;
}

int Heap::right(int i)
{
    return 2 * i + 2;
}

int Heap::left(int i)
{
    return 2 * i + 1;
}

/*
void Heap::set(int i, int v)
{
    if( i < length )
        a[i] = v;
}

int Heap::get(int i)
{
    assert(i < length);

    return a[i];
}
*/

void Heap::getHeap(vector<int>& b)
{
    b = a;
}


//
// exchange a[i] a[j]
//
void Heap::swap(int i, int j)
{
    int temp;

    temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}


void Heap::max_heapify(int i)
{
    int l, r, largest;

    l = left(i);
    r = right(i);
    largest = i;

    if( l < heap_size && a[i] < a[l] )
        largest = l;
    
    if (r < heap_size && a[largest] < a[r])
        largest = r;
    
    if( largest != i )
    {
        swap(i, largest);
        //cout << "swap: " << i << " -> " << largest << "\n";

        max_heapify(largest);
    }
}


void Heap::build_max_heap(void)
{
    int i;

    for( i = heap_size / 2 - 1; i >=0; i-- )
    {
        max_heapify(i);
    }
}


void Heap::heap_sort(void)
{
    build_max_heap();
    
    for( int i = length - 1; i >= 1; i-- )
    {
        // swap the top(max) to the bottom of heap
        swap(i, 0);
        heap_size = heap_size - 1; 

        max_heapify(0);
    }
}


void Heap::min_heapify(int i)
{
    int l, r, min;

    l = left(i);
    r = right(i);
    min = i;

    if( l < heap_size && a[i] > a[l] )
        min = l;
    
    if (r < heap_size && a[min] > a[r])
        min = r;
    
    if( min != i )
    {
        swap(i, min);
        //cout << "swap: " << i << " -> " << min << "\n";

        min_heapify(min);
    }
}


void Heap::build_min_heap(void)
{
    int i;

    for( i = heap_size / 2 - 1; i >=0; i-- )
    {
        min_heapify(i);
    }
}


void Heap::heap_sort_reverse(void)
{
    build_min_heap();

    print();
    
    for( int i = length - 1; i >= 1; i-- )
    {
        // swap the top(max) to the bottom of heap
        swap(i, 0);
        heap_size = heap_size - 1; 

        min_heapify(0);
    }
}


void Heap::print(void)
{
    for(int i = 0; i < length; i++ )
        cout << a[i] << " ";
    cout << "\n";
}


void Heap::min_heapify_with_new_element(int n)
{
    if( a[0] < n ) 
    {
        a[0] = n;
        min_heapify(0);
    }
}


// 
// find the top K elements in a[], which size is size_a
//
void top_k(const vector<int>& a, int k, vector<int>& b)
{
    // get the first k elements
    for( int i = 0; i < k; i++ )
        b.push_back(a[i]);
    
    Heap min_heap(b, k);
    
    //min_heap.print();
    min_heap.build_min_heap();
    //min_heap.print();

    for(int i = k; i < a.size(); i++)
    {
        min_heap.min_heapify_with_new_element(a[i]);
    }

    min_heap.getHeap(b);
}


template <class T>
void print_vector(const vector<T>& a)
{
    auto print = [](const T& n) {cout << n << ' ' ;};
    for_each(a.begin(), a.end(), print);

    cout << "\n";
}


int main(int argc, char* argv[])
{
    // cout << "hello world!\n";
    vector<int> a = {27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0};
    
    /*
    Heap heap_b(a, sizeof(a)/sizeof(a[0]));

    heap_b.print();
    heap_b.build_max_heap();
    heap_b.print();
    heap_b.heap_sort();
    heap_b.print();
    */

    /*
    Heap heap_a(a, a.size());
    heap_a.print();
    heap_a.heap_sort_reverse();
    heap_a.print();
    */

    print_vector(a);

    vector<int> b;
    top_k(a, 6, b);
 
    //auto print = [](const int& n) {cout << n << ' ' ;};
    //for_each(b.begin(), b.end(), print);
    print_vector(b);

    return 0;
}