//
// Created by zanbo on 2020/5/1.
//

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL || (!root->left && !root->right)) return root;
        TreeNode* newleft = invertTree(root->left);
        TreeNode* newright = invertTree(root->right);
        root->left = newright;
        root->right = newleft;
        return root;
    }
};