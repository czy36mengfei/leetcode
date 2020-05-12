//
// Created by zanbo on 2020/5/12.
//

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while(1)
        {
            if(root->val<p->val && root->val<q->val)
            {
                root = root->right;
            }
            else if(root->val>p->val && root->val>q->val)
            {
                root = root->left;
            }
            else
                return root;
        }
    }
};