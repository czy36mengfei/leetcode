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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        p = head
        pre = p
        p = p.next
        while p:
            if p.val == pre.val:
                pre.next = p.next
                p = p.next
            else:
                pre = p
                p = p.next
        return head


if __name__ == '__main__':
    while True:
        obj = Solution()
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        res_node = obj.deleteDuplicates(l1)
        res = list_node_to_list(res_node)
        print(res)
