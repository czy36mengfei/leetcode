class Solution {
public:
    // dp[i][0] 到第i个（不一定以i结尾）且最后2个是下降的最长子序列长度
    //  需要讨论i和i-1的大小关系
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        if(n==2 && nums[0]==nums[1]) return 1;
        if(n<=2) return n;
        vector<vector<int>> dp = vector<vector<int>>(n,vector<int>(2,1));
        for(int i=1;i<n;i++)
        {
            if(nums[i]>nums[i-1])
            {
                dp[i][0] = dp[i-1][0];
                dp[i][1] = max(dp[i-1][0]+1,dp[i-1][1]);
            }
            else if(nums[i]<nums[i-1])
            {
                dp[i][1] = dp[i-1][1];
                dp[i][0] = max(dp[i-1][1]+1,dp[i-1][0]);
            } else{
                dp[i][1] = dp[i-1][1];
                dp[i][0] = dp[i-1][0];
            }
        }
        return max(dp[n-1][0],dp[n-1][1]);
    }
};