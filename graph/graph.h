/*
《计算之魂》 工具与算法 

图的遍历，深度优先和广度优先

author: Jack Lee
date:   Aug 6, 2022 

file: graph.h
desc: define graph data structure

*/

#include <vector>
#include <string>

using namespace std;

typedef enum color 
{ 
    WHITE, 
    BLACK
} COLOR;


//
// define the EDGE, 
// 
//
typedef struct st_edge
{
    int  n_point_index; // the NO. of point. 
    int  n_weigth;      // the weigth of edge, ex: the distances between 2 points.
}EDGE;


//
// define point data structure, member
//  color - white if the point is not accessed, black is the opposite.
//
typedef struct st_point
{
    int   n_info;        // the info of the point
    COLOR point_color;   // white is the point has not been touched
    vector<EDGE> edges;  // the edges of this point
} POINT;


//
// class graph
//
class Graph {
    // data member
public:
    int             m_nPoint;   // the number of points
    vector<POINT>   m_Points; // the point list
    
    // methods operation
private:
    void DFT(int point_index);
    void DFT(int point_index, int level);

public:
    Graph(int n, int e_matrix[]);
    Graph(const string in[]);
    ~Graph();

    void touch(int index);
    void untouch(int index);
    void untouch_all(void);
    bool is_touch(int index);
    void depth_first_traverse(void);
    void breadth_first_traverse(void);
    void depth_first_traverse_level(void);
    void breadth_first_traverse_level(void);
};