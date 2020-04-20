//
// Created by zanbo on 2020/4/20.
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
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    string simplifyPath(string path) {
        if(path.size()<=1) return path;
        vector<string> myStack;
        int index = 1; //第一个字符一定是 /
        string temp = "";
        while(index<path.size())
        {
            while(index<path.size() && path[index]!='/')
            {
                temp+= path[index];
                index++;
            }
            // 三种情况 . or .. or other
            if(temp!="." && temp!=".." && temp!="")
            {
                myStack.push_back(temp);
            } else if(temp=="..")
            {
                if(!myStack.empty())
                {
                    myStack.pop_back();
                }
            }
            temp = "";
            // 去掉多余的/
            while(index<path.size() && path[index]=='/')
            {
                index++;
            }
        }
        // 遍历vector
        string res = "";
        for(int i=0;i<myStack.size();i++)
        {
            res += '/'+myStack[i];
        }
        if(res=="")
            res = "/";
        return res;
    }
};


int main()
{
    Solution s;
    string res = s.simplifyPath("///TJbrd/owxdG//");
    cout << res << endl;
}