//
// Created by zanbo on 2020/2/29.
//
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    //删除倒数第n个节点 使用两个指针 一个先走k步 再两个一起走
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        head = dummy;
        ListNode* cur = dummy;
        for(int i=0;i<n;i++)
            cur = cur->next;
        while(cur->next)
        {
            cur = cur->next;
            head = head->next;
        }
        head->next = head->next->next;
        return dummy->next;
    }
};