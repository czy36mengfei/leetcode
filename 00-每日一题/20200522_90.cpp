class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> temp;
        int n = nums.size();
        if(n==0)
        {
            res.push_back(temp);
            return res;
        }
        // sort 为了去重
        sort(nums.begin(),nums.end());
        helper(temp,nums,-1);
        return res;
    }
    void helper(vector<int>& temp,vector<int>& nums,int index)
    {
        res.push_back(temp);
        if(temp.size()==nums.size()) return;
        for(int i=index+1;i<nums.size();i++)
        {
            if(i!=index+1 && nums[i]==nums[i-1]) continue;
            temp.push_back(nums[i]);
            helper(temp,nums,i);
            temp.pop_back();
        }
    }
};