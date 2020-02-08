# 扁平化嵌套迭代器
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]  # 用栈，所以逆序
        self.value = None

    def next(self):
        """
        :rtype: int
        """
        # if self.hasNext():
        if self.value:
            return self.value

        # else:
        #     return
            # raise Exception("NestedList is empty")

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return False
        else:
            while self.stack:
                nest = self.stack.pop()
                if nest.isInteger():
                    self.value = nest.getInteger()
                    return True
                else:
                    self.stack.extend(nest.getList()[::-1])
        return False

if __name__ == '__main__':
    pass