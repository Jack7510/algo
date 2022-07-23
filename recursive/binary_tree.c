/*
《计算之魂》 思考题 2.2 
Q1. 修改中序遍历算法 2.2，将它变为先序遍历或者后序遍历算法

author: Jack Lee
date:   July 23, 2022
*/

#include <stdio.h>
#include <stdlib.h>


struct binary_tree
{
    void* data;         // any data
    struct binary_tree* left_subtree;   // point to left sub tree
    struct binary_tree* right_subtree;  // point to right sub tree
};


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
//
void depth_first_travers_tree_post(struct binary_tree* tree, 
    void(* func)(struct binary_tree *))
{
    if (NULL == tree) return;       // reach the end of leaf
    
    depth_first_travers_tree_post(tree->left_subtree, func);
    depth_first_travers_tree_post(tree->right_subtree, func);
    
    func(tree);
}


//
// build binary tree with the array a[]
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
// test function
//
int main(void)
{
    int a[] = {5, 2, 8, 0, 10, 7, 18, 20, 30, 12, 15, 1};
    struct binary_tree* tree = NULL;

    tree = build_binary_tree(a, sizeof(a)/sizeof(a[0]));
    
    printf("mid -> ");
    depth_first_travers_tree_mid(tree, print_node);
    printf("\n");

    printf("prev-> ");
    depth_first_travers_tree_prev(tree, print_node);
    printf("\n");

    printf("post-> ");
    depth_first_travers_tree_post(tree, print_node);
    printf("\n");

    free_binary_tree(tree);

    return 0;
}