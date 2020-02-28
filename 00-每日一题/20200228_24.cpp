//
// Created by zanbo on 2020/2/28.
//

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL) return head;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* pre = dummy;
        while(head && head->next)
        {
            pre->next = head->next;
            head->next = head->next->next;
            pre->next->next = head;
            pre = pre->next->next;
            head = head->next;
        }
        return dummy->next;
    }
};

