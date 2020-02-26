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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(-1)
        start.next = head
        cur = start
        index = 0
        while index < m-1:
            cur = cur.next
            index += 1
        m_pre = cur  # 第m-1个
        cur = cur.next
        n_last = cur  # 反转后的最后一个
        index += 1
        # 反转的部分
        pre = None
        while index <= n:
            next = cur.next
            cur.next = pre  # 反转
            pre = cur
            cur = next
            index += 1
        # 前接
        m_pre.next = pre
        # 后接
        n_last.next = cur
        return start.next


if __name__ == '__main__':
    while True:
        obj = Solution()
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        m_n_str = input().strip()
        m, n = list(map(int, m_n_str.split()))
        res_node = obj.reverseBetween(l1, m, n)
        res = list_node_to_list(res_node)
        print(res)