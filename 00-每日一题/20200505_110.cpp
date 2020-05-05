//
// Created by zanbo on 2020/5/5.
//

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        int height = 0;
        return helper(height,root);
    }
    bool helper(int& height,TreeNode* root)
    {
        height+=1;
        if(!root->left && !root->right) //叶节点
            return true;
        int lefth = height;
        int righth = height;
        bool leftr = helper(lefth,root->left);
        bool rightr = helper(righth,root->right);
        {
            height = max(lefth, righth);
            return leftr && rightr && abs(lefth - righth) <= 1;
        }
    }
};