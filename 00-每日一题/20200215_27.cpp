//
// Created by zanbo on 2020/2/15.
//
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int res=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]!=val)
                nums[res++] = nums[i];
        }
        return res;
    }
};
