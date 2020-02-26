//
// Created by zanbo on 2020/2/26.
//

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* lessHead = new ListNode(-1);
        ListNode* largeHead = new ListNode(-1);
        ListNode* less = lessHead;
        ListNode* large = largeHead;
        while(head)
        {
            if(head->val<x)
            {
                less->next = head;
                less = less->next;
            } else{
                large->next = head;
                large = large->next;
            }
            head = head->next;
        }
        less->next = largeHead->next;
        large->next = NULL;
        return lessHead->next;
    }
};

