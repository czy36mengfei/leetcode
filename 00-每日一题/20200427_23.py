from leetcode.list_node import ListNode, list_node_to_list, list_to_list_node
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if length == 0:
            return None
        queue = []

        for i in range(length):
            if lists[i]:
                # python3的heapq 不支持自定义类，所以用下标
                heapq.heappush(queue, (lists[i].val, i))

        start = ListNode(-1)
        p = start

        while queue:
            val, i = heapq.heappop(queue)
            node = lists[i]  # 把后面放到第一个对于的index
            p.next = node
            p = p.next
            if node.next:
                lists[i] = node.next
                heapq.heappush(queue, (node.next.val,i))
                # 接上去的那个点还不知道后面是什么
                node.next = None
        return start.next

    def _merge(self, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        if node1.val < node2.val:
            node1.next = self._merge(node1.next, node2)
            return node1
        else:
            node2.next = self._merge(node1, node2.next)
            return node2


    def _r_mergeKLists(self, lists, start, end):
        if start >= end:
            return lists[start]
        mid = (start + end) // 2
        listnode1 = self._r_mergeKLists(lists, start, mid)
        listnode2 = self._r_mergeKLists(lists, mid+1, end)
        return self._merge(listnode1, listnode2)


    def _mergeKLists(self, lists):
        length = len(lists)
        if length == 0:
            return None

        return self._r_mergeKLists(lists, 0, length-1)



if __name__ == '__main__':
    obj = Solution()
    while True:
        k = int(input())
        lists = []
        for _ in range(k):
            nums_str = input().strip().split()
            nums = list(map(int, nums_str))
            list_node = list_to_list_node(nums)
            lists.append(list_node)
        head = obj._mergeKLists(lists)
        res = list_node_to_list(head)
        print(res)

