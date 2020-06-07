class Solution {
public:
    // dp[i]= max((i-j)*j,dp[i-j]*j)
    int integerBreak(int n) {
        vector<int> dp = vector<int>(n+1,0);
        dp[1] = 1;
        dp[2] = 1;
        for(int i=3;i<=n;i++)
        {
            int temp = 0;
            for(int j=1;j<i;j++)
            {
                temp = max(temp,max(dp[i-j]*j,(i-j)*j));
            }
            dp[i] = temp;
        }
        return dp[n];
    }
};
