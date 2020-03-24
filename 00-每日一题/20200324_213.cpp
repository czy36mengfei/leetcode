//
// Created by zanbo on 2020/3/24.
//

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(!n) return 0;
        if(n==1) return nums[0];
        if(n==2) return max(nums[0],nums[1]);
        return max(helper(0,n-2,nums),helper(1,n-1,nums));
    }
    int helper(int l,int r,vector<int>& nums)
    {
        vector<int> dp(r-l+1);
        dp[0] = nums[l];
        dp[1] = max(dp[0],nums[l+1]);
        for(int i=2;i<=r-l;i++)
        {
            dp[i] = max(dp[i-2]+nums[i+l],dp[i-1]);
        }
        return dp[r-l];
    }
};