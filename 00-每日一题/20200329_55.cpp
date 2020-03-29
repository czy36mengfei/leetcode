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
public:
    bool canJump(vector<int>& nums) {
        int n=nums.size();
        int resIndex = 0;
        for(int i=0;i<n-1;i++)
        {
            if(resIndex<i)
                return false;
            resIndex = max(resIndex,i+nums[i]);
        }
        return resIndex>=n-1;
    }
};

int main()
{
    Solution2 s;
    vector<int> nums = {1,1,1,1,1};
    int res = s.findTargetSumWays(nums,3);
    cout << res << endl;
}
