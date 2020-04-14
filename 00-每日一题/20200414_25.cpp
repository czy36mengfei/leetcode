//
// Created by zanbo on 2020/4/14.
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
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
    // k个一组 反转链表
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k==1)
            return  head;
        //先确定链表长度  使用快指针
        ListNode* fast = head;
        int num = 0;
        while(fast && fast->next)
        {
            fast = fast->next->next;
            num++;
        }
        if(fast)
            num = 2*num+1;
        else
            num = 2*num;

        int reverse_num = num / k; //一共反转几段

        ListNode* dumpy = new ListNode(-1);
        ListNode* lasttail = dumpy;
        ListNode* tail = head;
        ListNode* p = tail->next;
        for(int i=0;i<reverse_num;i++)
        {
            p = tail->next;
            for(int j=0;j<k-1;j++)
                // 每段内反转k-1次
            {
                tail->next = p->next;
                p->next = head;
                head = p;
                p = tail->next;
            }
            lasttail->next = head;
            lasttail = tail;
            tail = tail->next;
            head = tail;
        }
        return dumpy->next;
    }
};





int main()
{
    Solution s;
    vector<int> a = {1,2,3,4,5};
    ListNode* head = new ListNode(-1);
    ListNode* p=head;
    for(int i=0;i<a.size();i++)
    {
        p->next = new ListNode(a[i]);
        p = p->next;
    }
    p->next = NULL;
    head = head->next;
    s.reverseKGroup(head,2);
}