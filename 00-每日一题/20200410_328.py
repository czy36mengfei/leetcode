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
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None or head.next.next is None:
            return head
        i = 0
        odd_head = ListNode(-1)
        even_head = ListNode(-1)
        o_p = odd_head
        e_p = even_head
        p = head
        while p:
            i += 1
            if i % 2 == 1:
                o_p.next = p
                o_p = o_p.next
            else:
                e_p.next = p
                e_p = e_p.next
            p = p.next
        e_p.next = None
        o_p.next = even_head.next
        return odd_head.next


if __name__ == '__main__':
    while True:
        obj = Solution()
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        res_node = obj.oddEvenList(l1)
        res = list_node_to_list(res_node)
        print(res)
