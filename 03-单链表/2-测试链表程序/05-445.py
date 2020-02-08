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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = list()
        stack2 = list()

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        now_node = None
        add = 0
        right_node = None
        while len(stack1) != 0 and len(stack2) != 0:
            num1 = stack1.pop()
            num2 = stack2.pop()
            val = num1 + num2 + add
            now_node = ListNode(val % 10)
            now_node.next = right_node
            right_node = now_node
            add = val // 10

        if len(stack1) != 0:
            last_list = stack1
        else:
            last_list = stack2
        while len(last_list) != 0:
            num = last_list.pop()
            val = num + add
            now_node = ListNode(val % 10)
            now_node.next = right_node
            right_node = now_node
            add = val // 10
        if add != 0:
            now_node = ListNode(add)
            now_node.next = right_node
        return now_node




if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        l2_str = input().strip()
        l2 = list(map(int, l2_str.split()))
        l2 = list_to_list_node(l2)
        res_node = obj.addTwoNumbers(l1, l2)
        res = list_node_to_list(res_node)
        print(res)
