//
// Created by zanbo on 2020/2/16.
//
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()<=2)
            return nums.size();
        int length = 0;
        int flag = 0;
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]!=nums[i-1])
            {
                nums[++length] = nums[i];
                flag=0;
            }
            else if(nums[i]==nums[i-1] && flag==0)
            {
                nums[++length] = nums[i];
                flag++;
            }
        }
        return length+1;
    }
};
