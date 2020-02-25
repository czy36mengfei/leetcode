//
// Created by zanbo on 2020/2/25.
//

#include <vector>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int x): val(x),next(NULL){}
};

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if(m==n) return head;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        head= dummy;
        for(int i=0;i<m-1;i++)
        {
            head = head->next;
        }
        ListNode* tail = head->next;
        ListNode* cur;
        for(int i=0;i<n-m;i++)
        {
            cur = tail->next;
            tail->next = cur->next;
            cur->next = head->next;
            head->next = cur;
        }
        return dummy->next;
    }
};


