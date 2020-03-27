#include <vector>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <stdio.h>
#include <fstream>
using namespace std;

class Solution {
    // 回溯法
public:
    int res=0;
    int findTargetSumWays(vector<int>& nums, int S) {
        helper(nums,0,0,S);
        return res;

    }
    void helper(vector<int>& nums,int index,int sum,int S)
    {
        if(index==nums.size())
        {
            if(sum==S)
                res +=1;
            return;
        }
        // 正
            helper(nums,index+1,sum+nums[index],S);
        // 负
            helper(nums,index+1,sum-nums[index],S);
    }
};


class Solution2 {
    // 动态规划 dp[i][j] 0-i个数中按规则和为j的方法数目
    // dp[i][j] = dp[i-1][j-nums[i+1]] + dp[i-1][j+nums[i-1]] 需要注意j的范围 2*sum+1
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = 0;
        for(int i=0;i<nums.size();i++)
        {
            sum+=nums[i];
        }
        vector<vector<int>> dp(nums.size(),vector<int>(2*sum+1,0));
        dp[0][sum+nums[0]]+=1; // 如果nums[0]=0
        dp[0][sum-nums[0]]+=1;
        for(int i=1;i<nums.size();i++)
        {
            for(int j=0;j<=2*sum;j++)
            {
                if(j-nums[i]>=0)
                    dp[i][j] += dp[i-1][j-nums[i]];
                if(j+nums[i]<=2*sum)
                    dp[i][j] += dp[i-1][j+nums[i]];
            }
        }
        if(S<=sum) // 如果只有一个元素
            return dp[nums.size()-1][sum+S];
        else
            return 0;
    }
};

int main()
{
    Solution2 s;
    vector<int> nums = {1,1,1,1,1};
    int res = s.findTargetSumWays(nums,3);
    cout << res << endl;
}
