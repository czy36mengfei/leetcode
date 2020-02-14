//
// Created by zanbo on 2020/2/14.
//

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()<=1)
            return nums.size();
        int res = 1;
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]>nums[i-1])
                nums[res++] = nums[i];
        }
        return res;
    }
};