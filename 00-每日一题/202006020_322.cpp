class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<int> dp = vector<int>(amount+1,10000); // dp[j] 和为j的最少数量
        dp[0] = 0;
        for(int i=0;i<n;i++)
        {
            for(int j= coins[i];j<=amount;j++)
            {
                dp[j] = min(dp[j],dp[j-coins[i]]+1);
            }
        }
        return dp[amount]==10000?-1:dp[amount];
    }
};