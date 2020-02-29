# 链表与双指针
# 1 --1+(k-1)--> k, k --k+(n-k)-->n
# 1 --1+(n-k) -- > n+1-k(倒数第k个)

from leetcode.list_node import ListNode, list_to_list_node, list_node_to_list


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        start = ListNode(-1)
        start.next = head
        # 倒数第n个是len+1-n, 所以要slow移len+1-n
        # fast最后到len，第二段移len+1-n, 所以第一段移 len-(len+1-n)=n-1
        fast = start
        for _ in range(n-1):
            fast = fast.next
            if fast is None: # 移了n-1步，保证有n个
                return None
        slow = start
        pre = start # 保存slow前面一个点
        while fast.next: # fast移到最后一个
            fast = fast.next
            pre = slow
            slow = slow.next

        pre.next = slow.next
        return start.next

if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        n = int(input().strip())
        res_node = obj.removeNthFromEnd(l1, n)
        res = list_node_to_list(res_node)
        print(res)
