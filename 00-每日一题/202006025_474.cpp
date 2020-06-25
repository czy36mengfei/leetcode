class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int len = strs.size();
        vector<vector<int>> dp = vector<vector<int>>(m+1,vector<int>(n+1,0));
        for(int i=0;i<len;i++)
        {
            int zero_num = 0;
            int one_num = 0;
            for(int j=0;j<strs[i].size();j++)
            {
                if(strs[i][j]=='1')
                    one_num+=1;
                else
                    zero_num+=1;
            }
            for(int p=m;p>=zero_num;p--)
            {
                for(int q=n;q>=one_num;q--)
                {
                    dp[p][q] = max(dp[p][q],dp[p-zero_num][q-one_num]+1);
                }
            }
        }
        return dp[m][n];
    }
};
