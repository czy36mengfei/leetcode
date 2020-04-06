//
// Created by zanbo on 2020/4/6.
//


#include <vector>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <stdio.h>
#include <fstream>

using namespace std;


class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        int n=p.size();
        if(s.size()<n) return res;
        int count = n; // count=0表示p中元素全部放入窗口中
        int hash[26] = {0};
        for(int i=0;i<p.size();i++)
            hash[p[i]-'a']+=1; // 每个字母出现多少次的映射
        int l=0;
        int r=0;
        // 初始窗口
        while(r<l+n)
        {
            if(hash[s[r]-'a']-->0)
            {
                count --;
            }
            r++;
        }
        r--;
        if(!count)
            res.push_back(l);
        while(r<s.size()-1)
        {
            if(hash[s[l]-'a']++ >=0)
            {
                count ++;
            }
            l++;
            r++;
            if(hash[s[r]-'a']-- > 0)
            {
                count --;
            }
            if(!count)
                res.push_back(l);
        }
        return res;
    }
};




int main()
{
    Solution s;
    vector<int> M = {5,2,6,1};
    s.findAnagrams("baa","aa");
}




