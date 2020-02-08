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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        now = head
        while now:
            next = now.next  # 保存下一个节点
            now.next = pre  # 把当前节点指向过去节点
            pre = now
            now = next  # 继续考虑下一个节点
        return pre  # 剩下的pre就是原来的末尾


if __name__ == '__main__':
    obj = Solution()
    l1_str = input().strip()
    l1 = list(map(int, l1_str.split()))
    l1 = list_to_list_node(l1)
    res_node = obj.reverseList(l1)
    res = list_node_to_list(res_node)
    print(res)







