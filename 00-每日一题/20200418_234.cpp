//
// Created by zanbo on 2020/4/19.
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
public:
    bool isPalindrome(ListNode* head) {
        if(!head || !head->next) return true;
        // 找到中点
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast->next && fast->next->next)
        {
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode* right = slow->next;
        slow->next = NULL;
        right = reverse(right);

        while(right)
        {
            if(right->val != head->val)
                return false;
            right = right->next;
            head = head->next;
        }
        return true;
    }
    ListNode* reverse(ListNode* head)
    {
        // 递归法反转链表
        if(!head->next)
            return  head;
        ListNode* newhead = reverse(head->next);
        head->next->next = head;
        head->next = NULL;
        return newhead;
    }
};
