
class UnionFind1:

    def __init__(self, n):
        self.count = n
        self.parent = []
        for i in range(n):
            self.parent.append(i)

    def find(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self.parent[p_root] = q_root
        self.count -= 1


class UnionFind2:
    # 基于size的优化
    def __init__(self, n):
        self.count = n
        self.parent = []
        self.size = []
        for i in range(n):
            self.parent.append(i)
            self.size.append(1)

    def find(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if self.size[p_root] > self.size[q_root]:
            # 较短的挂在较长的下面
            self.parent[q_root] = p_root
            self.size[p_root] += self.size[q_root]
        else:

            self.parent[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        self.count -= 1

class UnionFind3:
    # 基于rank的优化
    def __init__(self, n):
        self.count = n
        self.parent = []
        self.rank = []
        for i in range(n):
            self.parent.append(i)
            self.rank.append(1)

    def find(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if self.rank[p_root] > self.rank[q_root]:
            # 较短的挂在较长的下面，高度肯定差至少一，所以拼接后高度不变
            self.parent[q_root] = p_root

        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[p_root] = q_root
            self.rank[q_root] += 1
        self.count -= 1


class UnionFind4:
    # 路径压缩
    def __init__(self, n):
        self.count = n
        self.parent = []
        self.rank = []
        for i in range(n):
            self.parent.append(i)
            self.rank.append(1)

    def find(self, p):
        while self.parent[p] != p:
            # 它的parent不是根，就把它放在parent的parent下
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if self.rank[p_root] > self.rank[q_root]:
            # 较短的挂在较长的下面，高度肯定差至少一，所以拼接后高度不变
            self.parent[q_root] = p_root

        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[p_root] = q_root
            self.rank[q_root] += 1
        self.count -= 1

class UnionFind5:
    # 路径压缩
    def __init__(self, n):
        self.count = n
        self.parent = []
        self.rank = []
        for i in range(n):
            self.parent.append(i)
            self.rank.append(1)

    def find(self, p):
        while self.parent[p] != p:
            # 它的parent不是根，就把它放在parent的parent下
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if self.rank[p_root] > self.rank[q_root]:
            # 较短的挂在较长的下面，高度肯定差至少一，所以拼接后高度不变
            self.parent[q_root] = p_root

        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[p_root] = q_root
            self.rank[q_root] += 1
        self.count -= 1

class UnionFind6:
    # 路径压缩-递归
    def __init__(self, n):
        self.count = n
        self.parent = []
        self.rank = []
        for i in range(n):
            self.parent.append(i)
            self.rank.append(1)

    def find(self, p):
        if self.parent[p] != p:
            # 它的parent不是根，就把它放在parent的根下
            self.parent[p] = self.find(self.parent[p])

        return self.parent[p]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if self.rank[p_root] > self.rank[q_root]:
            # 较短的挂在较长的下面，高度肯定差至少一，所以拼接后高度不变
            self.parent[q_root] = p_root

        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[p_root] = q_root
            self.rank[q_root] += 1
        self.count -= 1


if __name__ == '__main__':
    obj = UnionFind2(5)
    print(obj.count)
    obj.union(3, 4)
    print(obj.count)
    obj.union(3, 2)
    print(obj.count)
