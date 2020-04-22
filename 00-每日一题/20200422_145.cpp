//
// Created by zanbo on 2020/4/22.
//
class Solution {
public:
    // 后序遍历 非递归 左右根
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        if(!root) return res;
        stack<pair<TreeNode*,bool>> myStack;
        myStack.push(make_pair(root,false));
        while(!myStack.empty())
        {
            TreeNode* temp = myStack.top().first;
            bool flag = myStack.top().second;
            myStack.pop();
            if( flag || (!temp->left && !temp->right))
            {
                res.push_back(temp->val);
            } else{
                myStack.push(make_pair(temp, true));
                if(temp->right)
                    myStack.push(make_pair(temp->right, false));
                if(temp->left)
                    myStack.push(make_pair(temp->left, false));
            }
        }
        return res;
    }
};


