//
// Created by zanbo on 2020/3/14.
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

struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int x): val(x),next(NULL){};
};


/**
 * Definition for a binary tree node.
 *  */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<string> res;
    vector<string> restoreIpAddresses(string s) {
        if(s.length()>12 || s.length()<4)
            return res;
        backtrace(s,"",0,0);
        return res;
    }

    void backtrace(string s, string temp,int index,int num)
    // s:输出字符串 不变    temp:当前生成的ip字符串    index:遍历到s的哪一个字符  num:temp中包含的ip段
    {
        // 定义返回条件
        if((4-num)*3<s.length()-index || (4-num)>s.length()-index) //后面字符数不够了或太多了 直接返回
            return;
        if(num==4 && index==s.length()){
            temp.pop_back();
            res.push_back(temp);
            return;
        }
        string ip ="";
        for(int i=index;i<=index+2 && i<s.length();i++)
        {
            ip = ip+s[i];
            // 没有考虑0的情况 0不能作为数字的开头 =======
            if(ip.length()>1 && ip[0] == '0')
                continue;
            if(atoi(ip.c_str())<=255)
                backtrace(s,temp+ip+".",i+1,num+1);
        }
    }
};


int main()
{
    Solution s;
    s.restoreIpAddresses("010010");

}

