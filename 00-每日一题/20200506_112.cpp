//
// Created by zanbo on 2020/5/6.
//

class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        return helper(root,sum,0);
    }

    bool helper(TreeNode* node, int& sum,int temp)
    {
        if(!node) return false;
        temp+=node->val;
        if(!node->left && !node->right){ //叶节点
            return temp==sum;
        }
        return helper(node->left,sum,temp) || helper(node->right,sum,temp);
    }
};
