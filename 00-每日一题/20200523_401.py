class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        hour_nums = [8, 4, 2, 1]
        minute_nums = [32, 16, 8, 4, 2, 1]
        if num <0 or num>10:
            return []
        for i in range(0, num+1):
            hour_list = self.choose_nums(hour_nums, i)
            minute_list = self.choose_nums(minute_nums, num-i)

            for hour in hour_list:
                if hour > 11:
                    continue
                for minute in minute_list:
                    if minute > 59:
                        continue
                    minute_str = str(minute)
                    ans = str(hour)+':'+'0'[:2-len(minute_str)]+minute_str
                    res.append(ans)
        return res


    def choose_nums(self, nums, max_len):
        if max_len == 0:
            return [0]
        res = []
        self.choose(nums, 0, [], max_len, res)
        return res

    def choose(self, nums, start, pre, max_len, res):
        if len(pre) == max_len:
            if sum(pre) == 32:
                print('d')
            res.append(sum(pre))
            return

        for i in range(start, len(nums)):
            pre.append(nums[i])
            self.choose(nums, i+1, pre, max_len, res)
            pre.pop()

if __name__ == '__main__':
    obj = Solution()
    while True:
        num = int(input())
        res = obj.readBinaryWatch(num)
        print(res)



