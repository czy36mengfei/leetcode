class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        last_nums = set()

        while True:
            sum = 0
            while n:
                h = n % 10
                sum += h ** 2
                n = n // 10
            if sum == 1:
                return True
            if sum in last_nums:
                return False
            n = sum
            last_nums.add(n)

if __name__ == '__main__':

    obj = Solution()
    while True:

        n = int(input().strip())
        res = obj.isHappy(n)
        print(res)