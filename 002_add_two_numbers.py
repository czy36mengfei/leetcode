"""
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.


    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
"""

def list_to_list_node(l):
    p = head = ListNode(-1)
    for v in l:
        p.next = ListNode(v)
        p = p.next
    return head.next

def list_node_to_list(list_node):
    l = []
    while list_node:
        l.append(list_node.value)
        list_node = list_node.next
    return l


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p = head = ListNode(-1)
        carry = 0
        while l1 and l2:

            p.next = ListNode(l1.value + l2.value+carry)
            carry = p.next.value // 10
            p.next.value = p.next.value % 10
            l1 = l1.next
            l2 = l2.next
            p = p.next

        last = l1 or l2
        while last:
            p.next = ListNode(last.value + carry)
            carry = p.next.value // 10
            p.next.value = p.next.value % 10
            last = last.next
            p = p.next
        if carry:
            p.next = ListNode(1)

        return head.next





if __name__ == '__main__':
    obj = Solution()
    l1_str = input().strip()
    l1 = list(map(int, l1_str.split()))
    l1 = list_to_list_node(l1)
    l2_str = input().strip()
    l2 = list(map(int, l2_str.split()))
    l2 = list_to_list_node(l2)
    res_node = obj.addTwoNumbers(l1, l2)
    res = list_node_to_list(res_node)
    print(res)
