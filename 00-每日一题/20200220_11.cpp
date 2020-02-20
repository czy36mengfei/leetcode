//
// Created by zanbo on 2020/2/20.
//

class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0;
        int j=height.size()-1;
        int res = min(height[i],height[j])*(j-i);
        while(i<j)
        {
            res = max(res,min(height[i],height[j])*(j-i));
            if(height[i]<=height[j])
                i++;
            else
                j--;
        }
        return res;
    }
};

