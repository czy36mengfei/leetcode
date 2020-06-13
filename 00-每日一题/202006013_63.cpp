class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        if(m==0) return m;
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp = vector<vector<int>>(m,vector<int>(n,0));
        dp[0][0] = obstacleGrid[0][0]==1?0:1;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(obstacleGrid[i][j]==1 || (i==0&&j==0))
                    continue;
                if(i==0)
                    dp[i][j] = (obstacleGrid[i][j-1]==0?1:0)*dp[i][j-1];
                else if(j==0)
                    dp[i][j] = (obstacleGrid[i-1][j]==0?1:0)*dp[i-1][j];
                else
                    dp[i][j] = (obstacleGrid[i-1][j]==0?1:0)*dp[i-1][j] +  (obstacleGrid[i][j-1]==0?1:0)*dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};