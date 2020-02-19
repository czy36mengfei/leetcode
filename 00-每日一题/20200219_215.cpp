//
// Created by zanbo on 2020/2/19.
//

class Solution2 {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return quicksort(nums,0,nums.size()-1,k);
    }

    int quicksort(vector<int>& nums,int l,int r,int k)
    {
        if(l>=r) return nums[l];
        int lt = partition(nums,l,r);
        if(lt == nums.size()-k)
            return nums[lt];
        else if(lt>nums.size()-k)
            return quicksort(nums,l,lt-1,k);
        else
            return  quicksort(nums,lt+1,r,k);
    }

    int partition(vector<int>&nums,int l,int r)
    {
        int i=l;
        int key = nums[l];
        for(int j=l+1;j<=r;j++)
        {
            if(nums[j]<key)
                swap(nums[++i],nums[j]);
        }
        swap(nums[l],nums[i]);
        return i;
    }

};