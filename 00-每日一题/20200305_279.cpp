//
// Created by zanbo on 2020/3/5.
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
    //从0到n的最短路径问题 使用图的广度优先搜索 BFS ==== test case 7168 超时！
public:
    int numSquares(int n) {
        queue<int> q;
        int step = 0;
        int curlevelcount = 1; //队列中当前层级节点个数 pop后需要减1 为0表示全部为下一层
        int nextlevelcount = 0; // next层个数 push后+1
        q.push(n);
        while(!q.empty())
        {
            int left = q.front();
            if(left == 0)
                return step;
            q.pop();
            curlevelcount--;
            for(int i=0;i<=int(sqrt(n));i++)
            {
                q.push(left-i*i);
                nextlevelcount++;
            }
            if(curlevelcount==0)
            {
                curlevelcount = nextlevelcount;
                nextlevelcount = 0;
                step++;
            }
        }
    }
    //动态规划
    int numSquares2(int n) {
        vector<int> dp(n + 1);
        for (int i = 1; i <= n; ++i) {
            dp[i] = i;
            for (int j = 1; j * j <= i; ++j)
                dp[i] = min(dp[i - j * j] + 1, dp[i]);
        }
        return dp[n];
    }
};



int main()
{
    Solution s;
    int res = s.numSquares(7168);
    cout<<res<<endl;
}