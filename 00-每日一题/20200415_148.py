from leetcode.list_node import ListNode, list_node_to_list, list_to_list_node


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            # 快慢指针找中点
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(head2)

        return self._combine(left, right)
    def _combine(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.val < right.val:
            left.next = self._combine(left.next, right)
            return left
        else:
            right.next = self._combine(left, right.next)
            return right


if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)

        res_node = obj.sortList(l1)
        res = list_node_to_list(res_node)
        print(res)
