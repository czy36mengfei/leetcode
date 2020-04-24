//
// Created by zanbo on 2020/4/24.
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


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    //偶数层 该层结果需要转置 可以使用reverse
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        vector<vector<int>> res;
        if(!root) return res;
        vector<int> temp; // 保存每层的结果
        q.push(root);
        int thislevel = 1;
        int nextlevel = 0;
        int odd = 0;
        while(!q.empty())
        {
            TreeNode* node = q.front();
            q.pop();
            temp.push_back(node->val);
            thislevel--;
            if(node->left) {
                q.push(node->left);
                nextlevel++;
            }
            if(node->right)
            {
                q.push(node->right);
                nextlevel++;
            }
            if(!thislevel)
            {
                //如果是偶数层 需要反转
                if(odd)
                {
                    reverse(temp.rbegin(),temp.rend());
                }
                odd = 1-odd;
                //该层遍历结束
                res.push_back(temp);
                thislevel = nextlevel;
                nextlevel = 0;
                temp.clear();
            }
        }
        return res;
    }
};

