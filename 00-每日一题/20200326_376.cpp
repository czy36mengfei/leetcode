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

class Solution { // dp[i][0]表示到第i个字符为止 最后一次是下降的 最长摇摆子序列的长度 （不一定以i结尾）
public:
    int wiggleMaxLength(vector<int>& nums) {
        int n=nums.size();
        if(n<2)
            return n;  // 1,17,5,10,13,15,10,5,16,8
        if(n==2 && nums[0]==nums[1])
            return 1;
        vector<vector<int>> dp(n,vector<int>(2,1));
        for(int i=1;i<n;i++)
        {
            //  上升
            if(nums[i]>nums[i-1])
            {
                dp[i][1] = dp[i-1][0] + 1;
                dp[i][0] = dp[i-1][0];
            }
            else if(nums[i]<nums[i-1])
            {
                dp[i][0] = dp[i-1][1] + 1;
                dp[i][1] = dp[i-1][1];
            } else
            {
                dp[i][0] = dp[i-1][0];
                dp[i][1] = dp[i-1][1];
            }
        }
        return max(dp[n-1][0],dp[n-1][1]);
    }
};

int main()
{
    Solution s;
    vector<int> nums = {1,17,5,10,13,15,10,5,16,8};
    int res = s.wiggleMaxLength(nums);
}
