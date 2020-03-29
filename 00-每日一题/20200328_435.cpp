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


bool const cmp(const vector<int>& x1, const vector<int>& x2) // &一定要加
{
    return x1[0]>x2[2];
}

class Solution {
    // 贪心思想
public:

    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if(intervals.size()<=1) return 0;
        //先按照起点排序
        sort(intervals.begin(),intervals.end());
        int res = 0;
        int end = intervals[0][1];
        for(int i=1;i<intervals.size();i++)
        {
            if(intervals[i][0]<end)
            {
                res++;
                // 如果终点在之前
                if(intervals[i][1]<end)
                    end = intervals[i][1];
            } else
                end = intervals[i][1];
        }
        return res;
    }
};

int main()
{
    Solution2 s;
    vector<int> nums = {1,1,1,1,1};
    int res = s.findTargetSumWays(nums,3);
    cout << res << endl;
}
