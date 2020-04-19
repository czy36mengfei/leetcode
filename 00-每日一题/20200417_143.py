# 链表与双指针
from leetcode.list_node import ListNode, list_to_list_node, list_node_to_list


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if head is None or head.next is None or head.next.next is None:
            return head
        # 使用快慢指针来平分链表
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = None
        # 逆序
        head2 = self._reverse(head2)
        k = 0
        head = self._merge(head, head2, k)
        return head

    def _merge(self, head1, head2, k):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if k % 2 == 0:
            k += 1
            head1.next = self._merge(head1.next, head2, k)
            return head1
        else:
            k += 1
            head2.next = self._merge(head1, head2.next, k)
            return head2

    def _reverse(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        # k = int(input().strip())
        res_node = obj.reorderList(l1)
        res = list_node_to_list(res_node)
        print(res)
