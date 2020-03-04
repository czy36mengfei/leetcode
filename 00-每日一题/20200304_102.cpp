//
// Created by zanbo on 2020/3/4.
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
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(!root) return res;
        queue<TreeNode*> q;
        int curlevel = 1; // 弹出一个节点 值--   值为0时表示到了下一层 值由nextlevel替换 next置0
        int nextlevel = 0; //push一个节点 值++
        //先放根结点
        q.push(root);
        vector<int> temp;
        while(!q.empty())
        {
            TreeNode* tempNode = q.front();
            temp.push_back(tempNode->val);
            if(tempNode->left)
            {
                q.push(tempNode->left);
                nextlevel++;
            }
            if(tempNode->right)
            {
                q.push(tempNode->right);
                nextlevel++;
            }
            q.pop();
            curlevel--;
            if(curlevel==0)
            {
                //先把前一层放入结果集 再清空temp
                res.push_back(temp);
                temp.clear();
                curlevel = nextlevel;
                nextlevel=0;
            }
        }
        return res;
    }
};
