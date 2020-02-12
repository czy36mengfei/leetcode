//
// Created by zanbo on 2020/2/12.
//


#include <vector>
#include <stdlib.h>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>

using namespace std;
class Solution {
    //贪心+二分查找
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size()<=1)
            return nums.size();
        int res=0;
        vector<int> temp; //辅助数组 其长度为最终结果
        temp.push_back(nums[0]);
        for(int i=1;i<nums.size();i++)
        {
            int key = nums[i];
            if(key>temp.back())
                temp.push_back(key);
            else
            {
                //二分查找 返回大于等于num[i]的第一个索引
                int l=0,r=temp.size()-1;
                while(l<r)
                {
                    int mid = (l+r)/2;
                    if(temp[mid]<key)
                        l = mid+1;
                    else
                        r = mid;
                }
                //修改temp数组
                temp[l] = key;
            }
        }
        cout<<temp.size()<<endl;
        return temp.size();
    }
};
int main()
{
    Solution s;
//    vector<int> vec = {-1, 2, 1, -4};
    vector<int> A = {10,9,2,5,3,7,101,18};
    s.lengthOfLIS(A);

}