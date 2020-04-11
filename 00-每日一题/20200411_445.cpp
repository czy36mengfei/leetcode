//
// Created by zanbo on 2020/4/11.
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
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1;
        stack<int> s2;
        stack<int> aggre;
        ListNode* head = NULL;
        //将两个链表分别放入栈中
        while(l1)
        {
            s1.push(l1->val);
            l1 = l1->next;
        }
        while(l2)
        {
            s2.push(l2->val);
            l2 = l2->next;
        }
//        int count = 0; // 进位
        int sum = 0;
        int first = 1;
        // 将两个栈代表的数字相加 加到新栈中
        while(!s1.empty() || !s2.empty())
        {
            if(!s1.empty())
            {
                sum +=  s1.top();
                s1.pop();
            }
            if(!s2.empty())
            {
                sum +=  s2.top();
                s2.pop();
            }
            ListNode* temp = new ListNode(sum%10);
            temp->next = head;
            head = temp;
            sum = sum/10;
        }
        // 最后还有进位
        if(sum)
        {
            ListNode* temp = new ListNode(sum);
            temp->next = head;
            head = temp;
        }
        return head;
    }
};