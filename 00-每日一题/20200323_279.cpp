//
// Created by zanbo on 2020/3/23.
//

class Solution {
    //从0到n的最短路径问题 使用图的广度优先搜索 BFS
public:
    int numSquares(int n) {
        if(!n) return 0;
        vector<int> dp(n+1);
        for(int i=1;i<=n;i++)
        {
            dp[i] = i;
            int temp = sqrt(i);
            for(int j=1;j<=temp;j++)
            {
                dp[i] = min(dp[i],dp[i-j*j]+1);
            }
        }
        return dp[n];
    }
};