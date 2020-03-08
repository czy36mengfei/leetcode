//
// Created by zanbo on 2020/3/8.
//


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
    /*
     * 计算完全二叉树的节点个数
     * 利用完全二叉树的特点 引申出两个性质：
     *  1. 一个树是完全二叉树，那么其左右子树也都是完全二叉树 [因此可以针对完全二叉树计算节点个数的方法进行递归]
     *  2. 可以通过判断右子树最左节点是否为空（即右子树的深度是否比其小）
     *      1）为空 右子树是满二叉树 直接根据深度计算
     *      2）不为空 左子树是满二叉树 直接根据深度计算
     */
public:
    int countNodes(TreeNode* root) {
        if(!root)
            return 0;
        if(!root->left && !root->right)
            return 1;
        int leftLevelofRoot = height(root);
        int leftLevelofRight = height(root->right);
        if(leftLevelofRight+1==leftLevelofRoot)
            return countNodes(root->right)+pow(2,leftLevelofRight);
        else
            return countNodes(root->left)+pow(2,leftLevelofRight);
    }

    int height(TreeNode* node)
    {
        if(!node)
            return 0;
        int res = 1;
        while(node->left)
        {
            res++;
            node = node->left;
        }
        return res;
    }
};