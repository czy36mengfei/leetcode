//
// Created by zanbo on 2020/5/4.
//

class Solution1 {
public:
    // recursively
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return helper(root->left,root->right);
    }
    bool helper(TreeNode* a,TreeNode* b)
    {
        if(!a&&!b) return true;
        if(!a&&b || a&&!b) return false;
        if(a->val!=b->val) return false;
        return helper(a->left,b->right) && helper(a->right,b->left);
    }
};
class Solution2 {
public:
    // iteratively
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        queue<TreeNode*> q1;
        queue<TreeNode*> q2;
        q1.push(root->left);
        q2.push(root->right);
        TreeNode* a;
        TreeNode* b;
        while(!q1.empty() || !q2.empty())
        {
            a = q1.front();
            q1.pop();
            b = q2.front();
            q2.pop();
            if(!a&&!b) continue;
            if((!a&&b) || (a&&!b)) return false;
            if(a->val!=b->val) return false;
            q1.push(a->left);
            q1.push(a->right);
            q2.push(b->right);
            q2.push(b->left);
        }
        return true;
    }

};