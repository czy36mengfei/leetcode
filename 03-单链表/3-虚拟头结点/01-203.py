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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start = ListNode(-1)
        start.next = head
        p = start
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return start.next

    # 递归写法
    def _removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        head.next = self._removeElements(head.next, val)
        return head.next if head.val == val else head






if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        val = int(input().strip())
        res_node = obj._removeElements(l1, val)
        res = list_node_to_list(res_node)
        print(res)
