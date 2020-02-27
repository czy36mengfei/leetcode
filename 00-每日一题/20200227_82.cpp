//
// Created by zanbo on 2020/2/27.
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
    ListNode(int x): val(x),next(NULL){};
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* cur = dummy;
        while(cur->next)
        {
            if(cur->next->next!=NULL && cur->next->next->val == cur->next->val)
            {
                //发现重复节点
                int val = cur->next->val;
                while(cur->next && cur->next->val==val)
                {
                    //一个一个删除节点
                    cur->next = cur->next->next;
                }
            } else
                cur = cur->next;
        }
        return dummy->next;
    }
};

