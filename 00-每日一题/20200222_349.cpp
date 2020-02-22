//
// Created by zanbo on 2020/2/22.
//
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size()==0 || nums2.size()==0)
            return {};
        vector<int> res;
        unordered_set<int> set1;
        unordered_set<int> setInter;
        for(int i=0;i<nums1.size();i++)
        {
            set1.insert(nums1[i]);
        }
        for(int i=0;i<nums2.size();i++)
        {
            if(set1.find(nums2[i])!=set1.end() && setInter.find(nums2[i])==setInter.end())
            {
                setInter.insert(nums2[i]);
                res.push_back(nums2[i]);
            }
        }
        return res;
    }
};


