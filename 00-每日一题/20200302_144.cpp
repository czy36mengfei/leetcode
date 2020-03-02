//
// Created by zanbo on 2020/3/2.
//

class Solution {
    //二叉树前序遍历 迭代法
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> myStack;
        if(root==NULL) return res;
        myStack.push(root);
        while(!myStack.empty())
        {
            TreeNode* temp = myStack.top();
            myStack.pop();
            res.push_back(temp->val); //根节点先放入结果集
            //右 左 子树分别进栈
            if(temp->right)
                myStack.push(temp->right);
            if(temp->left)
                myStack.push(temp->left);
        }
        return res;
    }
};
