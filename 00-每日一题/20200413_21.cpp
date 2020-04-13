//
// Created by zanbo on 2020/4/13.
//

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dumpy = new ListNode(-1);
        ListNode* p=dumpy;
        while(l1 && l2)
        {
            if(l1->val <= l2->val)
            {
                p->next = l1;
                l1 = l1->next;
            } else{
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        if(l1)
            p->next = l1;
        else
            p->next = l2;
        return dumpy->next;
    }
};