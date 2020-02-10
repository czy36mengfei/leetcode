//
// Created by zanbo on 2020/2/10.
//

class Solution {
public:
    int searchLeft(vector<int>&nums, int target)
    {
        int l=0,r=nums.size()-1;
        while(l<r)
        {
            int mid = (r+l)/2;
            if(nums[mid]<target)
                l = mid+1;
            else
                r = mid;
        }
        if(nums[l]==target)
            return l;
        else
            return -1;
    }
    int searchRight(vector<int>&nums, int target)
    {
        int l=0,r=nums.size()-1;
        while(l<r)
        {
            int mid = (r+l+1)/2;
            if(nums[mid]>target)
                r = mid-1;
            else
                l = mid;
        }
        if(nums[l]==target)
            return l;
        else
            return -1;
    }
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(nums.size()==0)
            return {-1,-1};
        int begin = searchLeft(nums,target);
        if(begin==-1)
            return {-1,-1};
        int end = searchRight(nums,target);
        return {begin,end};
    }
};