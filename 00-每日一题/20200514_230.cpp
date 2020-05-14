//
// Created by zanbo on 2020/5/13.
//

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int index=0;
    int res;
    int kthSmallest(TreeNode* root, int k) {
        helper(root,k);
        return res;
    }
    void helper(TreeNode* node,int& k)
    {
        if(node==NULL) return;
        helper(node->left,k);
        index+=1;
        if(index==k) {
            res = node->val;
        }
        if(index<k)
        {
            helper(node->right,k);
        }
    }
};