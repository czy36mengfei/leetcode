//
// Created by zanbo on 2020/4/21.
//

class Solution {
public:
    // 中序遍历 非递归
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if(!root)
            return res;
        stack<pair<TreeNode*,bool>> s;
        s.push(make_pair(root, false));
        while(!s.empty())
        {
            TreeNode* temp = s.top().first;
            bool flag = s.top().second;
            s.pop();
            if(flag)
            {
                res.push_back(temp->val);
            } else
            {
                if(temp->right)
                    s.push(make_pair(temp->right, false));
                s.push(make_pair(temp, true));
                if(temp->left)
                    s.push(make_pair(temp->left, false));
            }
        }
        return res;
    }
};