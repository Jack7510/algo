/*
《计算之魂》 思考题 2.2 
Q1. 修改中序遍历算法 2.2，将它变为先序遍历或者后序遍历算法

习题 2.3 Q2 回旋打印二叉树的节点
习题 2.4 Q1
习题 2.4 Q2

author: Jack Lee
date:   July 22, 2022 

History: 
date:   July 22, 2022   习题2.3 Q1, Q2
date:   July 23, 2022   习题2.4 Q1, Q2
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//
// 二叉树结构定义
//
typedef struct binary_tree
{
    void* data;         // any data
    struct binary_tree* left_subtree;   // point to left sub tree
    struct binary_tree* right_subtree;  // point to right sub tree
}BINARY_TREE;


//
// 队列结构定义
//
#define MAX_QUEUE 100
struct queue
{
    void* data[MAX_QUEUE];
    int   start_pointer;
    int   end_pointer;
};


void queue_init(struct queue* q)
{
    memset( q->data, 0, sizeof(void *) * MAX_QUEUE);
    q->start_pointer = 0;
    q->end_pointer   = 0;
}


//
// return 1: means queue is null, else return 0
//
int queue_is_null(struct queue* q)
{
    if( q->start_pointer == q->end_pointer )
        return 1;   // true
    else
        return 0;
}


//
// 没有考虑循环指针的情况
//
int queue_push_back(struct queue* q, void* p_data)
{
    if (q->end_pointer + 1 < MAX_QUEUE)
    {
        q->data[q->end_pointer] = p_data;
        q->end_pointer += 1;
        return 1;
    }
    
    return 0;
}


void* queue_pop_front(struct queue* q)
{
    if( queue_is_null(q) ) return NULL;

    return q->data[q->start_pointer++];
}


//
// stack definition and functions
//
#define MAX_STACK 100
struct stack
{
    void* data[MAX_STACK];
    int   top_pointer;
};


void stack_init(struct stack* s)
{
    memset( s->data, 0, sizeof(void *) * MAX_STACK);
    s->top_pointer = -1;
}

//
// return 1 if null, else return 0
//
int stack_is_null(struct stack* s)
{
    return s->top_pointer == -1 ;
}


int stack_push(struct stack* s, void* p)
{
    if( s->top_pointer + 1 >= MAX_STACK) return 0;

    s->top_pointer ++;
    s->data[s->top_pointer] = p;

    return 1;
}


void* stack_pop(struct stack* s)
{
    if( s->top_pointer == -1 ) return NULL;

    return s->data[s->top_pointer--];
}


//
// 处理节点信息，这里就是打印整数
//
void print_node( struct binary_tree* node )
{
    if (node != NULL)
        printf("%d ", (int)(node->data));
}


void free_node( struct binary_tree* node )
{
    if (node != NULL) free(node);
}

//
// 深度优先，中序遍历: 先遍历左子树，再处理根节点，最后遍历右子树
//
void depth_first_travers_tree_mid(struct binary_tree* tree, 
    void(* func)(struct binary_tree *))
{
    if (NULL == tree) return;       // reach the end of leaf

    depth_first_travers_tree_mid(tree->left_subtree, func);
    func(tree);
    depth_first_travers_tree_mid(tree->right_subtree, func);
}


//
// 深度优先，先序遍历：先处理根节点信息，再先遍历左，右子树
//
void depth_first_travers_tree_prev(struct binary_tree* tree, 
    void(* func)(struct binary_tree *))
{
    if (NULL == tree) return;       // reach the end of leaf
    
    func(tree);
    depth_first_travers_tree_prev(tree->left_subtree, func);
    depth_first_travers_tree_prev(tree->right_subtree, func);
}


//
// 深度优先，后序遍历：先遍历左，右子树，再处理根节点信息，
// history:
//  为了完成思考题 2.4Q1，增加计算tree的深度部分
//
int depth_first_travers_tree_post(struct binary_tree* tree, 
    void(* func)(struct binary_tree *))
{
    int depth_left = 0;
    int depth_right = 0;

    if (NULL == tree) return 0;       // reach the end of leaf
    
    depth_left = depth_first_travers_tree_post(tree->left_subtree, func);
    depth_right = depth_first_travers_tree_post(tree->right_subtree, func);
    
    func(tree);

    return ((depth_left > depth_right) ? depth_left : depth_right) + 1;
}


//
// build binary tree with the array a[]
// 比节点小的，放在左边，大的放在右边
//
void insert_node(struct binary_tree** p_tree, struct binary_tree* node)
{
    if (NULL == *p_tree )   // is root
    {
        *p_tree = node;
        return;
    }

    // if data > x, insert to left
    if ((int)((*p_tree)->data) >= (int)node->data )
    {
        insert_node(&((*p_tree)->left_subtree), node);
    }
    else
    {
        // data < x, insert to right
        insert_node(&((*p_tree)->right_subtree), node);
    }
}


struct binary_tree* build_binary_tree(int a[], int n)
{
    struct binary_tree* root = NULL;
    int i;

    for (i = 0; i < n; i++)
    {
        struct binary_tree* node;

        //
        // init node
        //
        node = malloc(sizeof(struct binary_tree));
        if (NULL == node) return NULL;

        node->data = (void*)a[i];
        node->left_subtree = NULL;
        node->right_subtree = NULL;

        insert_node(&root, node);
    }

    return root;
}


//
// free the tree memory
//
void free_binary_tree(struct binary_tree* tree)
{
    if (NULL == tree) return;       // reach the end of leaf
    
    depth_first_travers_tree_post(tree, free_node);
}


//
// 广度优先遍历二叉树
//
void breadth_first_traverse_tree(struct binary_tree* tree, 
    void(* func)(struct binary_tree *))
{
    struct queue q;

    if (NULL == tree) return;

    queue_init( &q );
    queue_push_back( &q, tree);

    while (!queue_is_null(&q))
    {
        struct binary_tree* node;

        node = (struct binary_tree*) queue_pop_front(&q);
        func(node);

        if( node->left_subtree != NULL ) {    // left tree is not null
            queue_push_back(&q, (void*)node->left_subtree);
        }

        if( node->right_subtree != NULL ) {
            queue_push_back(&q, (void*)node->right_subtree);
        }
    }
}


//
// 思考题 2.3 Q2 回旋打印二叉树的节点
// 修改二叉树的广度遍历算法，使得偶数行的节点从左向右遍历，奇数行的节点从右向左遍历
// 思路：偶数行用队列queue(FIFO)，奇数行用堆栈stack(LIFO)
//
void breadth_first_traverse_tree_q2(struct binary_tree* tree, 
    void(* func)(struct binary_tree *))
{
    struct queue q;
    int    line = 0;
    struct stack s0, s1;

    if (NULL == tree) return;

    //queue_init( &q );
    //queue_push_back( &q, tree);
    stack_init( &s0 );
    stack_push( &s0, tree);
    stack_init( &s1 );

    while (!stack_is_null(&s0))
    {
        while (!stack_is_null(&s0))
        {
            struct binary_tree* node;

            node = (struct binary_tree*) stack_pop(&s0);
            func(node);

            // 奇数行的节点，从左向右压入堆栈, 弹出时，就是从右到做
            if( node->left_subtree != NULL ) {    // left tree is not null
                stack_push(&s1, (void*)node->left_subtree);
            }

            if( node->right_subtree != NULL ) {
                stack_push(&s1, (void*)node->right_subtree);
            }
        }

        while ( !stack_is_null(&s1) )
        {
            struct binary_tree* node;

            node = (struct binary_tree*) stack_pop(&s1);
            func(node);

            // 偶数行的节点，从右向左压入堆栈，弹出时，就是从左到右
            if( node->right_subtree != NULL ) {    // left tree is not null
                stack_push(&s0, (void*)node->right_subtree);
            }

            if( node->left_subtree != NULL ) {
                stack_push(&s0, (void*)node->left_subtree);
            }
        }   
    }
}


//
// 思考题 2.4 Q2 如何在一个二叉排序树中找到第二大的元素
// 1. 实现找到最大元素
// 2. 实现找到指定元素的前一个 predecessor
//
int tree_max(struct binary_tree* root, 
    struct binary_tree** x,             // return the max node
    struct binary_tree** x_parent)
{
    if ( root == NULL ) return 0;

    if ( root->right_subtree == NULL )
    {
        *x = root;
        return 1;    
    }

    *x_parent = root;
    return tree_max(root->right_subtree, x, x_parent);
}


struct binary_tree* tree_predecessor(struct binary_tree* root, // the root of the tree
    struct binary_tree* x,             // the node whose precessor would be found 
    struct binary_tree* x_parent)       // the parent of x
{
    struct binary_tree * predecessor = NULL;
    struct binary_tree * tmp_parent;
    
    if ( root == NULL || x == NULL ) return NULL;

    // if left subtree is not null, return the max of left tree
    if( x->left_subtree != NULL )
    {
        tree_max(x->left_subtree, &predecessor, &tmp_parent );
        return predecessor;
    }

    return x_parent;
}


//
// test function
//
int main(void)
{
    int a[] = {5, 2, 8, 0, 10, 7, 18, 20, 30, 12, 15, 1, 22, 11};
    struct binary_tree* tree = NULL;
    struct binary_tree *node, *parent, *predecessor;
    
    int depth_tree = 0;

    tree = build_binary_tree(a, sizeof(a)/sizeof(a[0]));
    
    printf("mid -> ");
    depth_first_travers_tree_mid(tree, print_node);
    printf("\n");

    printf("prev-> ");
    depth_first_travers_tree_prev(tree, print_node);
    printf("\n");

    printf("post-> ");
    depth_tree = depth_first_travers_tree_post(tree, print_node);
    printf("\n");
    printf("2.4 Q1-> %d\n", depth_tree);

    printf("breath->");
    breadth_first_traverse_tree(tree, print_node);
    printf("\n");

    printf("2.3 Q2->");
    breadth_first_traverse_tree_q2(tree, print_node);
    printf("\n");

    printf("2.4 Q2->");
    node = NULL;
    parent = NULL;
    predecessor = NULL;
    tree_max(tree, &node, &parent);
    predecessor = tree_predecessor(tree, node, parent);
    printf("max = %d, parent = %d, predecessor = %d\n", 
        (int)node->data, (int)parent->data, (int)predecessor->data);

    free_binary_tree(tree);

    return 0;
}