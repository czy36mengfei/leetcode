//
// Created by zanbo on 2020/3/11.
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
    /*
     * 二叉排序树 删除节点 1）先查找 返回节点指针 & 父指针 & 是左还是右子树 2）再删除节点
     */
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode* dummy = new TreeNode(-1);
        dummy->left = root;
        TreeNode* temp = root;
        TreeNode* fa = dummy;
        int isleft = -1; // 1: 左子树 0：右子树
        int found = 0; // 1:查找成功
        // ============== 查找 =========
        while(temp)
        {
            if(temp->val==key){
                found = 1;
                break;
            }
            fa = temp;
            if(temp->val>key){
                temp = temp->left;
                isleft = 1;
            }
            else{
                temp = temp->right;
                isleft = 0;
            }
        }

        // ============== 删除 =================

        //如果未查找成功 直接返回
        if(!found) return root;
        //如果是temp是叶子节点 直接删除即可
        if(!temp->left && !temp->right){
            if(isleft==1)
                fa->left = NULL;
            else if(isleft==0)
                fa->right = NULL;
            else //只有根结点一个节点
                return NULL;
        } else if(!temp->left) {
            //如果左子树为空
            if (isleft == 1 || isleft == -1)
                fa->left = temp->right;
            else if (isleft == 0)
                fa->right = temp->right;
        }
        else if(!temp->right) {
            //如果右子树为空
            if (isleft == 1 || isleft == -1)
                fa->left = temp->left;
            else if (isleft == 0)
                fa->right = temp->left;
        } else{
            //左右都不空 找左子树的最右节点
            TreeNode * leftRight = temp->left;
            TreeNode* fa = temp;
            while(leftRight->right)
            {
                fa = leftRight;
                leftRight = leftRight->right;
            }
            int num = leftRight->val;
            //如果是叶子
            if(!leftRight->left)
            {
                if(fa==temp) fa->left=NULL;
                else fa->right = NULL;
            }
            else{
                if(fa==temp) fa->left=leftRight->left;
                else fa->right = leftRight->left;
            }
            temp->val = num;
        }
        return dummy->left;
    }
};

class Solution2
{
    // 递归的写法
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(!root) return NULL;
        if(key < root->val)
        {
            root->left = deleteNode(root->left,key);
        }
        else if(key > root->val)
        {
            root->right = deleteNode(root->right,key);
        } else{
            //分情况讨论  是叶子节点 or 左子树右子树都为空 or 有一颗子树为空
            if(!root->left && !root->right)
            {
                return NULL;
            }
            else if(root->left && root->right){
                //需要找右子树的最小节点 赋值 且删除那个节点
                TreeNode* temp = root->right;
                while(temp->left)
                {
                    temp = temp->left;
                }
                int num = temp->val;
                root->val = num;
                root->right = deleteNode(root->right,num); //此处又调用一次删除节点的函数
            } else{
                if(root->left && !root->right) // 右子树为空
                    return root->left;
                else
                    return root->right;
            }
        }
        return root;
    }
};

int main()
{
    Solution2 s;
    vector<int> x = {1,2,3,4};

    TreeNode* t1 = new TreeNode(3);
    TreeNode* t2 = new TreeNode(1);
    TreeNode* t3 = new TreeNode(4);
    TreeNode* t4 = new TreeNode(2);
    TreeNode* t5 = new TreeNode(4);
    TreeNode* t6 = new TreeNode(7);

    TreeNode* t7 = new TreeNode(7);
    TreeNode* t8 = new TreeNode(2);
    TreeNode* t9 = new TreeNode(5);
    TreeNode* t10 = new TreeNode(1);
    t1->left = t2;
    t1->right = t3;
    t2->right = t4;
//    t2->right = t5;
//    t3->right = t6;
//    t4->right = t8;
//    t6->left = t9;
//    t6->right = t10;

    TreeNode* node = s.deleteNode(t1,3);

}

