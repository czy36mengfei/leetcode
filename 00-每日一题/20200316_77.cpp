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
    vector<vector<int>> res;
    vector<vector<int>> combine(int n, int k) {
        vector<int> temp;
        backtrace(n,k,temp,0);
        return res;
    }

    void backtrace(int n,int k,vector<int> temp,int now)
    {
        if(temp.size()==k)
        {
            res.push_back(temp);
            return;
        }
        for(int i=now+1;i<=n;i++)
        {
            temp.push_back(i);
            backtrace(n,k,temp,i);
            temp.pop_back();
        }

    }

};
