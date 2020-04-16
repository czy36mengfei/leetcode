from leetcode.list_node import ListNode, list_node_to_list, list_to_list_node


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        start = ListNode(-1)
        start.next = head
        p = head


        while p.next:
            find = start
            cur = p.next  # 拿出要插入的点
            p.next = cur.next
            while find != p and cur.val > find.next.val:  # 到p之前还未找到
                find = find.next
            # 因为找到跳出
            if find != p:
                # 将其放在find和find.next之间
                next = find.next
                cur.next = next
                find.next = cur
            # 没有找到退出
            else:
                # 将其放在最后
                p.next = cur
                p = p.next

        return start.next

    def _insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        start = ListNode(-1)
        start.next = head

        cur = head
        while True:
            while cur.next and cur.val < cur.next.val:
                cur = cur.next  # 前面是有序的
            if cur.next is None:
                break
            node = cur.next
            pre = start
            while pre.next.val < node.val:
                pre = pre.next

            cur.next = node.next
            node.next = pre.next
            pre.next = node
        return start.next



if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)

        res_node = obj._insertionSortList(l1)
        res = list_node_to_list(res_node)
        print(res)
