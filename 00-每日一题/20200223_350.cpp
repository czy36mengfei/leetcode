#include <vector>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;


class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> myMap;
        vector<int> res;
        for(int x:nums1)
        {
            myMap[x]+=1;
        }
        for(int x:nums2){
            if(myMap[x]>0)
            {
                res.push_back(x);
                myMap[x]--;
            }
        }
        return res;
    }
};

// 如果两个数组都是排好序的 应该怎么做
class Solution2 {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        int i=0,j=0;
        while(i<nums1.size()&&j<nums2.size())
        {
            if(nums1[i]==nums2[j])
            {
                res.push_back(nums1[i]);
                i++;
                j++;
            }
            else if(nums1[i]<nums2[j])
            {
                i++;
            }
            else
                j++;
        }
        return res;
    }
};

int main()
{
    Solution s;
    vector<int> a = {1,2,4,5,7,100};
    vector<int> b = {0,2,2,98};
    vector<int> c = s.intersect(a,b);
    for(int i=0;i<c.size();i++)
        cout << c[i] << endl;
}
