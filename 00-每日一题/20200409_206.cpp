#include <vector>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <stdio.h>
#include <fstream>

using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next) return head;
        ListNode* p=head;
        ListNode* pnext;
        while(p->next)
        {
            pnext = p->next;
            p->next = pnext->next;
            pnext->next = head;
            head = pnext;
        }
        return head;
    }
};




int main()
{
    Solution s;
    vector<int> M = {5,2,6,1};
    s.lengthOfLongestSubstring("pwwkew");
}
