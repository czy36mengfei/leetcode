from leetcode.list_node import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return
        if node.next is None:
            node = None
            return


        # 把后一个往前拷贝，再把后一个删除，这样就可以解决不知道前面节点的问题
        dele_node = node.next
        node.val = dele_node.val
        node.next = dele_node.next
        dele_node =None

