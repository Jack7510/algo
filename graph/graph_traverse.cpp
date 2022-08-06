/*
《计算之魂》 工具与算法 

图的遍历，深度优先和广度优先

author: Jack Lee
date:   Aug 6, 2022 

version 1: 深度优先，广度优先算法
version 2: 思考题 5.2 Q1

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
// constructor from string input
//
Graph::Graph(const string in[])
{
    m_nPoint = stoi(in[0]);
    int edges = stoi(in[1]);
    
    for(int i = 0; i < m_nPoint; i++ )
    {
        POINT p;

        p.point_color = WHITE;
        m_Points.push_back(p);
    }

    for(int i = 2; i < (edges * 2 + 2); i++)
    {
        EDGE e;
        int u, v;
        string::size_type pos;

        u = stoi(in[i]);
        pos = in[i].find(' ');
        v = stoi(in[i].substr(pos + 1));

        e.n_point_index = v - 1;
        m_Points[u-1].edges.push_back(e);
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


void Graph::DFT(int point_index, int level)
{
    // if point has been touched, do nothing
    if( is_touch(point_index) ) return;

    touch(point_index);
    // point_index + 1, make it easy to review the graph
    cout << point_index + 1 << "\t" << "level: " << level << "\n";

    // traverse all edges with reverse 
    for( EDGE e : m_Points[point_index].edges )
    {
        if( !is_touch(e.n_point_index) )
            DFT(e.n_point_index, level + 1);
    }

    //cout << "\n";
}


//
// 深度优先遍历, 带level
//
void Graph::depth_first_traverse_level(void)
{
    // 从第一个点开始
    DFT(0, 1);
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
// 广度优先遍历, 把点在哪一层都打印出来
//
struct st_point_info
{
    int  n_index;   // 点的号码
    int  n_level;   // 点的层次
};

void Graph::breadth_first_traverse_level(void)
{
    list<struct st_point_info> q;
    struct st_point_info s, t;
    int level = 0;

    s.n_index = 0;
    s.n_level = 1;
    q.push_back(s);     // handle the first element

    while (!q.empty())
    {
        t = q.front();
        q.pop_front();

        if( is_touch(t.n_index) )
            continue;   // if the point is touched, do nothing
        
        touch(t.n_index);
        if( t.n_level > level )
        {
            level = t.n_level;
            cout << "\nlevel :" << level << "\n";
        }
        cout << t.n_index + 1 << " ";
        
        // push all the points connecting with index to the queue
        for( EDGE e : m_Points[t.n_index].edges )
        {
            s.n_index = e.n_point_index;
            s.n_level = t.n_level + 1;
            if( !is_touch(e.n_point_index) )
                q.push_back(s);
        }
    }
    
    cout << "\n";
}


//
// test
//
int main()
{
    /*
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
    */

    const string str_grpah[] = { // 2E + 2
        "13",   // number of vertex
        "21",   // number of edge
        "1 2",  // edge(1,2)
        "1 3",
        "2 4",
        "2 5",
        "2 6",
        "2 7",
        "2 1",
        "3 7",
        "3 8",
        "5 9",
        "5 10",
        "5 6",
        "6 5",
        "6 10",
        "6 11",
        "6 8",
        "6 7",
        "6 2",
        "7 6",
        "7 8",
        "7 3",
        "7 2",
        "8 3",
        "8 7",
        "8 6",
        "8 11",
        "8 12",
        "9 13",
        "9 11",
        "9 10",
        "9 5",
        "10 12",
        "10 6",
        "10 5",
        "10 9",
        "11 8",
        "11 6",
        "11 9",
        "12 8",
        "12 10",
        "12 13",
        "13 12",
        "13 9"
    };

    //Graph g(n, edge_matrix);
    Graph g(str_grpah);

    //g.depth_first_traverse();
    //g.untouch_all();

    g.depth_first_traverse_level();
    g.untouch_all();

    //g.breadth_first_traverse();
    //g.untouch_all();

    g.breadth_first_traverse_level();
    g.untouch_all();
    
    return 0;
}
