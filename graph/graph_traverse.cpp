/*
《计算之魂》 工具与算法 

图的遍历，深度优先和广度优先

author: Jack Lee
date:   Aug 6, 2022 

*/

#include <iostream>
#include <iterator>
#include <list>

#include "graph.h"

using namespace std;

//
// constructor
//
Graph::Graph(int n, int e_matrix[])
{
    m_nPoint = n;

    for(int i = 0; i < n; i++)
    {
        POINT p;

        p.point_color = WHITE;
        for( int j = 0; j < n; j++ )
        {
            // add edge(i,j)
            if( e_matrix[i * n + j] ) // there is an edge
            {
                EDGE e;
                e.n_point_index = j;    // e(i, j)
                p.edges.push_back(e);
            }
        }

        // add point "i"
        m_Points.push_back(p);
    }
}


//
// de-constructor
//
Graph::~Graph(void)
{
    for( POINT p : m_Points )
    {
        p.edges.clear();
    }

    m_Points.clear();
}


//
// touch, set color -> black, means it has been accessed
//
void Graph::touch(int index)
{
    m_Points[index].point_color = BLACK;
}

void Graph::untouch(int index)
{
    m_Points[index].point_color = WHITE;
}

void Graph::untouch_all(void)
{
    for( int i = 0; i < m_nPoint; i++ )
    {
        untouch(i);
    }
}

//
// is_touch, return true if the point has been accessed
//
bool Graph::is_touch(int index)
{
    return m_Points[index].point_color == BLACK;
}


//
// 深度优先遍历
//
void Graph::depth_first_traverse(void)
{
    // 从第一个点开始
    DFT(0);
}

//
// 从当前的点开始，逆时针遍历
//
void Graph::DFT(int point_index)
{
    // if point has been touched, do nothing
    if( is_touch(point_index) ) return;

    touch(point_index);
    // point_index + 1, make it easy to review the graph
    cout << point_index + 1 << " ";

    // traverse all edges with reverse 
    for( EDGE e : m_Points[point_index].edges )
    {
        if( !is_touch(e.n_point_index) )
            DFT(e.n_point_index);
    }

    cout << "\n";
}

//
// 广度优先遍历
//
void Graph::breadth_first_traverse(void)
{
    list<int> q;

    q.push_back(0);     // handle the first element

    while (!q.empty())
    {
        int index = q.front();
        q.pop_front();

        if( is_touch(index) )
            continue;   // if the point is touched, do nothing
        
        touch(index);
        cout << index + 1 << " ";
        
        // push all the points connecting with index to the queue
        for( EDGE e : m_Points[index].edges )
        {
            if( !is_touch(e.n_point_index) )
                q.push_back(e.n_point_index);
        }
    }
    
    cout << "\n";
}



//
// test
//
int main()
{
    int n = 13;         // 13 个点
    int edge_matrix[] = {
    //  1  2  3  4  5  6  7  8  9 10 11 12 13
        0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,     // 1
        1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0 ,     // 2
        1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ,     // 3
        0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,     // 4
        0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0 ,     // 5
        0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0 ,     // 6
        0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0 ,     // 7
        0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0 ,     // 8
        0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1 ,     // 9
        0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0 ,     // 10
        0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0 ,     // 11
        0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1 ,     // 12
        0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0       // 13
    };

    Graph g(n, edge_matrix);
    g.depth_first_traverse();
    
    g.untouch_all();
    g.breadth_first_traverse();

    return 0;
}
