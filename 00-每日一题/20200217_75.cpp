//
// Created by zanbo on 2020/2/17.
//

class Solution {
public:
    void sortColors(vector<int>& nums) {
        partition(nums,0,nums.size()-1);
    }

    void partition(vector<int>& nums,int l, int r)
    {
        if(l>=r) return;
        int i=l;
        int key = nums[l];
        for(int j=l+1;j<=r;j++)
        {
            if(nums[j]<=key)
                swap(nums[j],nums[++i]);
        }
        swap(nums[l],nums[i]);
        partition(nums,l,i-1);
        partition(nums,i+1,r);
    }

};