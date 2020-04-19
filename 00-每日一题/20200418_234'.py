# 链表与双指针
from leetcode.list_node import ListNode, list_to_list_node, list_node_to_list


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        stack = list()
        fast = head
        slow = head
        stack.append(slow.val)
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
        if fast.next is None:
            # 奇数
            stack.pop()

        p = slow.next
        while p:
            if p.val != stack.pop():
                return False
            p = p.next
        return True


if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        # k = int(input().strip())
        res_node = obj.isPalindrome(l1)
        print(res_node)
        # res = list_node_to_list(res_node)
        # print(res)
