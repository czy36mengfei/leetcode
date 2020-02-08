# 动态规划 重叠子问题与记忆化搜索
memory = None
def _fib(n):
    if n == 1:
        memory[n] = 0
        return memory[n]
    if n == 2:
        memory[n] = 1
        return memory[n]

    if memory[n] != -1:
        return memory[n]
    memory[n] = _fib(n-1) + _fib(n-2)
    return memory[n]


if __name__ == '__main__':
    while True:
        n = int(input())
        memory = [-1 for i in range(n+1)]
        res = _fib(n)
        print(res)