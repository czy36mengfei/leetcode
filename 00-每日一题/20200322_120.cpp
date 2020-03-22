//
// Created by zanbo on 2020/3/22.
//

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> dp(n+1,0);
        for(int row=n-1;row>=0;row--)
        {
            for(int col=0;col<=row;col++)
            {
                dp[col] = min(dp[col],dp[col+1])+triangle[row][col];
            }
        }
        return dp[0];
    }
};
