# 链表与双指针
from leetcode.list_node import ListNode, list_to_list_node, list_node_to_list


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k < 1:
            return head

        length = 1
        p = head
        while p.next:
            p = p.next
            length += 1

        p.next = head
        # 设head是第1位
        # 移k位后的最后一位是 倒数第k+1位， 整数 n+1-(k+1)=n-k 位
        # 从head 第1位 到n-k位， 需要移动n-k-1位
        p = head
        k = k % length
        for i in range(length-k-1):
            p = p.next
        # 最后一位的下一位是后面的head，并把中间指针断掉
        new_head = p.next
        p.next = None
        return new_head


if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        k = int(input().strip())
        res_node = obj.rotateRight(l1, k)
        res = list_node_to_list(res_node)
        print(res)
