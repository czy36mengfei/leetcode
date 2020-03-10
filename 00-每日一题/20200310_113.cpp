//
// Created by zanbo on 2020/3/10.
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

/**
* Definition for a binary tree node.
* struct TreeNode {
*     int val;
*     TreeNode *left;
*     TreeNode *right;
*     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
* };
*/

class Solution { // 回溯法 深度优先 push - 回溯 - pop
public:
    vector<vector<int>> res;
    int remain;
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if(!root) return res; // 初始输入为空 要特判
        vector<int> temp;
        remain = sum;
        path(root,temp);
        return res;
    }

    void path(TreeNode* node,vector<int>& temp)
    {
        if(!node->left && !node->right)  //如果是叶子结点
        {
            //先判断是否合法
            if(remain-(node->val)==0)
            {
                temp.push_back(node->val);
                res.push_back(temp);
                temp.pop_back();
            }
            return;
        }
        // if(remain-node->val<=0) //不是叶子结点 且和已经大于sum 无需继续递归  nono 负数！！
        //     return;
        temp.push_back(node->val);
        remain -= node->val;
        if(node->left)
        {
            path(node->left,temp);
        }
        if(node->right)
        {
            path(node->right,temp);
        }
        //回溯
        temp.pop_back();
        remain += node->val;
        return;
    }
};
int main()
{
    Solution s;
    vector<int> x = {1,2,3,4};

    TreeNode* t1 = new TreeNode(-2);
    TreeNode* t2 = new TreeNode(-3);
    TreeNode* t3 = new TreeNode(8);
    TreeNode* t4 = new TreeNode(11);
    TreeNode* t5 = new TreeNode(13);
    TreeNode* t6 = new TreeNode(4);
    TreeNode* t7 = new TreeNode(7);
    TreeNode* t8 = new TreeNode(2);
    TreeNode* t9 = new TreeNode(5);
    TreeNode* t10 = new TreeNode(1);
    t1->right = t2;
//    t1->right = t3;
//    t2->left = t4;
//    t3->left = t5;
//    t3->right = t6;
//    t4->left =  t7;
//    t4->right = t8;
//    t6->left = t9;
//    t6->right = t10;

    vector<vector<int>> res = s.pathSum(t1,-5);

}