//
// Created by zanbo on 2020/3/7.
//

class Solution {
public:
    int minDepth(TreeNode* root) { // BFS 广度优先遍历
        if(root==NULL)
            return 0;
        if(!root->left && !root->right)
            return 1;
        queue<TreeNode*> q;
        q.push(root);
        int curCount = 1;
        int nextCount = 0;
        int res = 1;
        while(!q.empty())
        {
            TreeNode* temp = q.front();
            if(!temp->left && !temp->right) //叶子结点
                return res +1;
            q.pop();
            curCount--;
            if(temp->left) {
                q.push(temp->left);
                nextCount++;
            }
            if(temp->right)
            {
                q.push(temp->right);
                nextCount++;
            }
            if(curCount==0)
            {
                //开始新一层
                res ++;
                curCount = nextCount;
                nextCount = 0;
            }
        }
    }


};

class Solution2 {
public:
    int minDepth(TreeNode* root) { // DFS 递归 深度优先遍历
        if(!root) return 0;
        if(!root->left) return minDepth(root->right)+1;
        if(!root->right) return minDepth(root->left)+1;
        return 1+min(minDepth(root->right),minDepth(root->left));
    }
};