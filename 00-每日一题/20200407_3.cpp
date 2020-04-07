//
// Created by zanbo on 2020/4/7.
//

class Solution {
    //返回最长的无重复字符的子串长度：使用滑动窗口的方法
public:
    int lengthOfLongestSubstring(string s) {
        int myMap[256]; // 使用int数组做哈希表 不用map char一共256
        memset(myMap,-1, sizeof(myMap));
        int l=0;
        int r=0;
        int maxLen = 0;
        for(;r<s.size();r++)
        {
            if(myMap[s[r]]<l)
            {
                //之前未出现过
                // 记录目前的长度
                maxLen = max(maxLen,r-l+1);
            } else{
                // 遇到重复字符 需要移动左边界
                l = myMap[s[r]]+1;

            }
            myMap[s[r]] = r;
        }
        return maxLen;
    }
};

