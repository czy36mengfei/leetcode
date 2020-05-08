//
// Created by zanbo on 2020/5/8.
//

class Solution {
public:
    int sum=0;
    int sumNumbers(TreeNode* root) {
        if(root==NULL) return sum;
        helper(root,"");
        return sum;
    }

    void helper(TreeNode* node,string temp)
    {
        if(node==NULL) return;
        temp+= to_string(node->val);
        if(node->right==NULL && node->left==NULL)
        {
            int inttemp = atoi(temp.c_str());
            sum += inttemp;
            return;
        }
        helper(node->left,temp);
        helper(node->right,temp);
        return;
    }
};