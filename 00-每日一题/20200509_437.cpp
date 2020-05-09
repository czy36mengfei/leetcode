//
// Created by zanbo on 2020/5/9.
//
class Solution {
public:
    int res=0;
    int pathSum(TreeNode* root, int sum) {
        unordered_map<int,int> temp;
        temp[0]=1;
        helper(root,sum,0,temp);
        return res;
    }
    void helper(TreeNode* node,int& sum,int val,unordered_map<int,int>& temp) //保存从根节点到后续某节点的路径和，对应的个数
    {
        if(node==NULL) return;
        val += node->val;
        if(temp[val-sum]>0) {
            res += temp[val - sum];
        }
        temp[val]++;
        helper(node->left,sum,val,temp);
        helper(node->right,sum,val,temp);
        temp[val]--;
    }
};

