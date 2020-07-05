class Solution {
public:
    // dp[i][j] : 前i个 和为 j 的总情况数
    // dp[i][j] = dp[i-1][j-a[i]] + dp[i-1][j+a[i]
    // 返回 dp[n-1][S+1000]
    int findTargetSumWays(vector<int>& nums, int S) {
        int n = nums.size();
        int sum = 0;
        for(int i=0;i<n;i++)
        {
            sum+=nums[i];
        }
        if(S>sum) return 0;
        vector<vector<int>> dp = vector<vector<int>>(n,vector<int>(2*sum+1,0));
        dp[0][sum+nums[0]]+=1;
        dp[0][sum-nums[0]]+=1; // nums[0]=0的特例
        for(int i=1;i<n;i++)
        {
            for(int j=0;j<2*sum+1;j++)
            {
                if(j-nums[i]>=0)
                    dp[i][j] += dp[i-1][j-nums[i]];
                if(j+nums[i]<=2*sum)
                    dp[i][j] += dp[i-1][j+nums[i]];
            }
        }
        return dp[n-1][S+sum];
    }
};