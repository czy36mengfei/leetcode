//
// Created by zanbo on 2020/3/9.
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
public:
    int sumOfLeftLeaves(TreeNode* root) {
        return sum(root,0);
    }

    int sum(TreeNode* node,int flag)
    {
        if(!node) return 0;
        if(!node->left && !node->right && flag)
            return node->val;
        return sum(node->left,1)+sum(node->right,0);
    }
};
