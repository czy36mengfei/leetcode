//
// Created by zanbo on 2020/4/17.
//

class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head || !head->next) return;
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

        ListNode* dumpy = new ListNode(-1);
        ListNode* p = dumpy;
        while(right)
        {
            p->next = head;
            head  =head->next;
            p = p->next;
            p->next = right;
            right = right->next;
            p = p->next;


        }
        if(head)
        {
            p->next = head;
        }
        head = dumpy->next;
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
