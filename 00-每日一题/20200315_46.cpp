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
    // 需要记录哪些数字已经走过 还剩哪些没有走 ==== 不需要用set 只用一个bool数组即可
public:
    vector<vector<int>> res;
    vector<vector<int>> permute(vector<int>& nums) {
        if(!nums.size()) return res;
        vector<int> temp;
//        set<int> remain(nums.begin(),nums.end());
        bool visited[nums.size()];
        memset(visited,false, sizeof(visited));
        backtrace(temp,visited,nums);
        return res;
    }

    void backtrace(vector<int> temp,bool* visited,vector<int> nums) // temp:已组成的排列 remain：原数组中剩下的数字
    {
        if(temp.size()==nums.size())
        {
            res.push_back(temp);
            return;
        }
        for(int i=0;i<nums.size();i++)
        {
            if(visited[i])
                continue;
            temp.push_back(nums[i]);
            visited[i] = true;
            backtrace(temp,visited,nums);
            //返回原始状态
            temp.pop_back();
            visited[i] = false;
        }
        return;
    }
};


int main()
{
    Solution s;
    s.restoreIpAddresses("010010");

}

