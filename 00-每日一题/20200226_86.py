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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_head = ListNode(-1)
        big_head = ListNode(-1)
        s_p = small_head
        b_p = big_head
        p = head
        while p:
            if p.val < x:
                s_p.next = p
                s_p = s_p.next
            else:
                b_p.next = p
                b_p = b_p.next
            p = p.next

        b_p.next = None
        s_p.next = big_head.next
        return small_head.next


if __name__ == '__main__':
    while True:
        obj = Solution()
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        x = int(input().strip())
        res_node = obj.partition(l1, x)
        res = list_node_to_list(res_node)
        print(res)
