//
// Created by zanbo on 2020/2/11.
//
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l=0,r=nums.size();
        int mid;
        while(l<r)
        {
            mid = (l+r)/2;
            if(nums[mid]<target)
                l = mid+1;
            else
                r = mid;
        }
        return l;
    }
};

