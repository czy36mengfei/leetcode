//
// Created by zanbo on 2020/4/10.
//

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode* odd_dumpy=new ListNode(-1);
        ListNode* even_dumpy=new ListNode(-1);
        ListNode* odd = odd_dumpy;
        ListNode* even = even_dumpy;
        int index = 1;
        while(head)
        {
            if(index&1) // odd
            {
                odd->next = head;
                odd = odd->next;
            } else{
                even->next = head;
                even = even->next;
            }
            head = head->next;
            index +=1;
        }
        odd->next = even_dumpy->next;
        even->next=NULL;
        return odd_dumpy->next;
    }
};
