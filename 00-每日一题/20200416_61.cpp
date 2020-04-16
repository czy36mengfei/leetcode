//
// Created by zanbo on 2020/4/16.
//


class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || !head->next) return head;
        //首先使用快指针计算链表长度
        ListNode* fast = head;
        int i=1;
        int len=0;
        while(fast->next && fast->next->next)
        {
            fast = fast->next->next;
            i++;
        }
        if(!fast->next)
        {
            len = 2*i-1;
        }else{
            //偶数
            len = 2*i;
            fast = fast->next; // fast现在是链表尾节点指针 为后面rotate做准备
        }
        int m = k%len;
        if(!m) return head; // 不用变化

        ListNode* p = head;
        for(int i=1;i<len-m;i++)
        {
            p=p->next;
        }
        ListNode* newhead = p->next;
        p->next = NULL;
        fast->next = head;
        return newhead;
    }
};