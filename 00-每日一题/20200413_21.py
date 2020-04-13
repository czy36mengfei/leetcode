# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_list_node(l):
    p = head = ListNode(-1)
    for v in l:
        p.next = ListNode(v)
        p = p.next
    return head.next


def list_node_to_list(list_node):
    l = []
    while list_node:
        l.append(list_node.val)
        list_node = list_node.next
    return l


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        l2_str = input().strip()
        l2 = list(map(int, l2_str.split()))
        l2 = list_to_list_node(l2)
        res_node = obj.mergeTwoLists(l1, l2)
        res = list_node_to_list(res_node)
        print(res)
