//
// Created by zanbo on 2020/2/21.
//
class Solution{
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int i=0;
        int j=0;
        int sum = 0;
        int res = INT_MAX;
        for(int j=0;j<nums.size();j++)
        {
            sum+= nums[j];
            if(sum>=s) {
                while(sum>=s)
                {
                    sum-=nums[i];
                    i++;
                }
                res = min(res,j-i+2);
            }
        }
        if(res==INT_MAX)
            return 0;
        return res;
    }
};
