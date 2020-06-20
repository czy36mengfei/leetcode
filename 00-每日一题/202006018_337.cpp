struct result{
    int include;
    int not_include;
};
class Solution {
public:
    int rob(TreeNode* root) {
        result r = helper(root);
        return max(r.include,r.not_include);
    }
    result helper(TreeNode* root)
    {
        if(root == NULL){
            result res;
            res.include = 0;
            res.not_include = 0;
            return res;
        }
        int include = 0;
        int not_include = 0;
        result lr = helper(root->left);
        result rr = helper(root->right);
        include = root->val + lr.not_include + rr.not_include;
        not_include = max(lr.not_include,lr.include)+max(rr.not_include,rr.include);
        result res;
        res.include = include;
        res.not_include = not_include;
        return res;
    }
};