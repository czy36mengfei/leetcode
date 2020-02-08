# bowbit = i & (-i) = 2 ^ k (k表示最右边第k位)
# i=00100100 -1=11011100(11011011+1) 所以右边的一个1和往后的0会被保留
# 3 + lowbit(3) = 4  往最右的1加1，则再往左连续的1都变成0，第一个0变成1
# 0011 + 0001 = 0100

# i节点父节点的索引公式：parent(i)=i+lowbit(i)


class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.father = [0 for _ in range(n+1)]

    def _low_bit(self, x):
        return x & (-x)

    def update(self, index, delta):
        while index < self.size:
            # 更新当前节点的C值（用于前缀和计算）
            self.father[index] += delta
            # 计算收其影响的C
            index = index + self._low_bit(index)

    def query(self, index):
        res = 0
        while index > 0:
            res += self.father[index]
            index = index - self._low_bit(index)
        return res


