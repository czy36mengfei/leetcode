//
// Created by zanbo on 2020/5/7.
//

class Solution {
public:
    vector<string> res;
    vector<string> binaryTreePaths(TreeNode* root) {
        if(root==NULL) return res;
        helper(root,"");
        return res;
    }

    void helper(TreeNode* node,string temp)
    {
        if(node==NULL) return;
        temp+= "->"+to_string(node->val);
        if(node->right==NULL && node->left==NULL)
        {
            temp = temp.substr(2,temp.size()-2);
            res.push_back(temp);
            return;
        }
        helper(node->left,temp);
        helper(node->right,temp);
        return;
    }
};