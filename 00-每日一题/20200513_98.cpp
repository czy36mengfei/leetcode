//
// Created by zanbo on 2020/5/13.
//

class Solution {
public:
    long long pre = LONG_MIN;
    bool isValidBST(TreeNode* root) {
        // 中序遍历 当前是否比前一个大
        if(root==NULL) return true;
        if(!isValidBST(root->left)) return false;
        if(root->val<=pre)  return false;
        pre = root->val;
        return isValidBST(root->right);
    }

};