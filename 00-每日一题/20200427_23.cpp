//
// Created by zanbo on 2020/4/27.
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


//struct TreeNode {
//    int val;
//    TreeNode *left;
//    TreeNode *right;
//    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//};

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        //两两合并
        int n = lists.size();
        if(n==0) return NULL;
        if(n==1) return lists[0];
        while(n>1)
        {
            int k = (n+1)/2; //注意奇偶区别 细节
            for(int i=0;i<n/2;i++)
            {
                lists[i] = mergetwo(lists[i],lists[i+k]);
            }
            n = k;
        }
        return lists[0];
    }
    ListNode* mergetwo(ListNode* l1,ListNode* l2)
    {
        ListNode* dumpy = new ListNode(-1);
        ListNode* p = dumpy;
        while(l1 && l2)
        {
            if(l1->val<=l2->val){
                p->next = l1;
                l1= l1->next;
            } else{
                p->next = l2;
                l2= l2->next;
            }
            p = p->next;
        }
        if(l1){
            p->next = l1;
        }
        if(l2){
            p->next = l2;
        }
        return dumpy->next;
    }
};

