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
    //和层次遍历的区别：1.先右后左 2.每层只取第一个放到结果集
    vector<int> rightSideView(TreeNode* root) {
        queue<TreeNode*> q;
        vector<int> res;
        if(!root) return res;
        q.push(root);
        int thislevel = 1;
        int nextlevel = 0;
        while(!q.empty())
        {
            int first = 1;
            //每一层的第一个
            while(!q.empty() && thislevel)
            {
                TreeNode* node = q.front();
                q.pop();
                thislevel--;
                if(first) {
                    res.push_back(node->val);
                    first = 0;
                }
                if(node->right)
                {
                    q.push(node->right);
                    nextlevel++;
                }
                if(node->left) {
                    q.push(node->left);
                    nextlevel++;
                }
            }
            //该层遍历结束
            thislevel = nextlevel;
            nextlevel = 0;
        }
        return res;
    }
};
