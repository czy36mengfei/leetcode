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
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> temp;
        backtrace(candidates,target,temp,0,0);
        return res;
    }
    void backtrace(vector<int>& candidates,int target,vector<int>temp,int index,int sum)
    {
        if(sum==target)
        {
            res.push_back(temp);
            return;
        }
        for(int i=index;i<=candidates.size()-1;i++)
        {
            if(sum+candidates[i]>target)
                continue;
            temp.push_back(candidates[i]);
            backtrace(candidates,target,temp,i,sum+candidates[i]);
            temp.pop_back();
        }
    }


};
