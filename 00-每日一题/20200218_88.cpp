//
// Created by zanbo on 2020/2/18.
//
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for(int i=0;i<n;i++)
        {
            nums1[m+i] = nums2[i];
        }
        //对nums1排序 - 使用快排
        partition(nums1,0,m+n-1);
    }
    void partition(vector<int>& nums,int l,int r)
    {
        if(l>=r) return;
        int i=l;
        int key=nums[l];
        for(int j=l+1;j<=r;j++)
        {
            if(nums[j]<key)
                swap(nums[++i],nums[j]);
        }
        swap(nums[l],nums[i]);

        partition(nums,l,i-1);
        partition(nums,i+1,r);
    }

};
